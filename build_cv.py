"""
build_cv.py – Génère CV_Kouadio_Cedric.pdf en deux étapes :
  1. Playwright  : HTML → PDF A4 avec rendu Chromium
  2. reportlab + pypdf : injection d'un bloc ATS invisible (texte blanc Helvetica 1pt)
     correctement encodé et extractible par tous les parseurs PDF des ATS.
"""
import asyncio
import base64
import io
import re
import tempfile
from pathlib import Path

from playwright.async_api import async_playwright
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter

HTML_PATH  = Path(__file__).parent / "CV_Cedric_Kouadio.html"
PDF_PATH   = Path(__file__).parent / "CV_Cedric_Kouadio.pdf"
PHOTO_PATH = Path(__file__).parent / "Me.jpeg"

ATS_KEYWORDS = (
    "Data Analyst Data Scientist Big Data Intelligence Artificielle IA Automatisation "
    "Machine Learning Deep Learning NLP traitement langage naturel Python pandas numpy "
    "scikit-learn matplotlib seaborn FastAPI Flask LangChain LangGraph RAG FAISS BM25 "
    "embeddings vector database TensorFlow PyTorch Keras BERT GPT transformers "
    "huggingface OpenAI LLM prompt engineering fine-tuning Java Spring Boot Spring "
    "Security JPA Hibernate Maven Gradle Lombok REST API SOAP microservices Laravel "
    "PHP Eloquent MVC Blade C# .NET Docker Kubernetes Jenkins GitHub Actions CI/CD "
    "DevOps MLOps ETL pipeline Airflow dbt Spark Kafka Hadoop SQL MySQL PostgreSQL "
    "SQL Server MongoDB Redis Cassandra ElasticSearch NoSQL Git GitHub GitLab pull "
    "request code review Swagger OpenAPI Postman pytest unittest JUnit Mockito TDD BDD "
    "Agile Scrum Kanban sprint Figma UX UI responsive Tableau Power BI Looker Metabase "
    "AWS S3 EC2 Lambda Azure Blob Storage Google Cloud GCP BigQuery Vertex AI Firebase "
    "alternance stage Ile-de-France Paris data science data engineering feature "
    "engineering model deployment monitoring drift AB testing statistics regression "
    "classification clustering PCA anomaly detection time series forecasting scoring "
    "chatbot computer vision OCR Selenium BeautifulSoup scraping Excel VBA reporting "
    "dashboard KPI visualisation nettoyage donnees data quality RGPD conformite "
    "securite JWT OAuth2 RBAC authentification autorisation chiffrement HTTPS SSL TLS "
    "OWASP API Gateway caching load balancing nginx Linux Bash scripting automatisation "
    "processus RPA NER sentiment analysis summarization recommendation text mining "
    "text classification named entity recognition computer vision image processing"
)


def create_ats_overlay() -> io.BytesIO:
    """
    Génère une page PDF avec les mots-clés ATS en texte blanc Helvetica 1pt.
    Invisible visuellement (blanc sur blanc), mais correctement encodé :
    les parseurs PDF des ATS l'extraient proprement.
    """
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    # Texte blanc — invisible sur fond blanc
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica", 1)

    # Découper en lignes de ~100 caractères
    words = ATS_KEYWORDS.split()
    lines, current = [], []
    for word in words:
        current.append(word)
        if len(" ".join(current)) >= 100:
            lines.append(" ".join(current))
            current = []
    if current:
        lines.append(" ".join(current))

    # Écrire en bas de page (hors zone de contenu visible)
    text_obj = c.beginText(2, 6)
    text_obj.setFont("Helvetica", 1)
    text_obj.setFillColorRGB(1, 1, 1)
    for line in lines:
        text_obj.textLine(line)
    c.drawText(text_obj)

    c.save()
    buf.seek(0)
    return buf


def create_photo_layer() -> "io.BytesIO | None":
    """Injecte la photo directement dans le PDF à la résolution native (928×928 px → ~790 DPI).
    Chromium plafonne les images à ~150 DPI ; ce contournement donne une netteté maximale."""
    if not PHOTO_PATH.exists():
        return None

    from PIL import Image as PILImage
    from reportlab.lib.utils import ImageReader

    W, H = A4  # 595.28 × 841.89 pt

    # CSS print → pt : 1 CSS px @ 96 dpi = 0.75 pt
    # Photo : 112 px, padding header : 11 px haut / 22 px droite
    r_pt = 112 * 0.75 / 2        # 42 pt
    cx   = W - 22 * 0.75 - r_pt  # 536.78 pt (centre X)
    cy   = H - 11 * 0.75 - r_pt  # 791.64 pt (centre Y, origine bas-gauche)

    # Crop carré centré sur le visage (miroir de object-position: center 5%)
    with PILImage.open(PHOTO_PATH) as im:
        iw, ih = im.size          # 928 × 1130
        s    = min(iw, ih)        # 928
        left = (iw - s) // 2     # 0
        top  = int(ih * 0.01)    # ≈ 11 px depuis le haut
        top  = max(0, min(top, ih - s))
        im_sq = im.crop((left, top, left + s, top + s)).convert("RGB")
        img_buf = io.BytesIO()
        im_sq.save(img_buf, "PNG")
        img_buf.seek(0)

    ir = ImageReader(img_buf)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    # Clip circulaire + dessin de l'image pleine résolution
    c.saveState()
    clip = c.beginPath()
    clip.circle(cx, cy, r_pt)
    c.clipPath(clip, stroke=0, fill=0)
    c.drawImage(ir, cx - r_pt, cy - r_pt, width=2 * r_pt, height=2 * r_pt)
    c.restoreState()

    # Bordure dorée (#e94560) dessinée hors du clip
    c.setStrokeColorRGB(233 / 255, 69 / 255, 96 / 255)
    c.setLineWidth(1.5)
    c.circle(cx, cy, r_pt, stroke=1, fill=0)

    c.save()
    buf.seek(0)
    return buf


def embed_images(html: str, base_dir: Path) -> str:
    """Remplace src="fichier.ext" par des data URI base64 pour forcer la pleine résolution.
    Les JPEG sont convertis en PNG lossless pour éviter la double compression dans le PDF."""
    def replacer(m):
        src = m.group(1)
        if src.startswith("http") or src.startswith("data:"):
            return m.group(0)
        img_path = base_dir / src
        if not img_path.exists():
            return m.group(0)
        if src.lower().endswith((".jpg", ".jpeg")):
            from PIL import Image as _Image
            buf = io.BytesIO()
            with _Image.open(img_path) as im:
                im.save(buf, format="PNG", optimize=False)
            data = base64.b64encode(buf.getvalue()).decode()
            return f'src="data:image/png;base64,{data}"'
        data = base64.b64encode(img_path.read_bytes()).decode()
        return f'src="data:image/png;base64,{data}"'
    return re.sub(r'src="([^"]+)"', replacer, html)


async def build():
    # ── Étape 1 : Playwright → PDF ────────────────────────────
    # Intégrer les images en base64 pour la pleine résolution dans le PDF
    html_content = HTML_PATH.read_text(encoding="utf-8")
    html_embedded = embed_images(html_content, HTML_PATH.parent)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(device_scale_factor=3)
        page = await context.new_page()
        await page.set_content(html_embedded, wait_until="networkidle")
        await page.pdf(
            path=str(PDF_PATH),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
    print(f"[1/3] PDF Playwright   : OK")

    # ── Étape 2 : photo haute résolution via reportlab ────────
    photo_buf   = create_photo_layer()
    overlay_buf = create_ats_overlay()
    reader      = PdfReader(str(PDF_PATH))
    writer      = PdfWriter()

    main_page = reader.pages[0]
    if photo_buf:
        main_page.merge_page(PdfReader(photo_buf).pages[0])
    main_page.merge_page(PdfReader(overlay_buf).pages[0])
    writer.add_page(main_page)

    # Conserver les pages suivantes si elles existent
    for extra in reader.pages[1:]:
        writer.add_page(extra)

    with open(str(PDF_PATH), "wb") as f:
        writer.write(f)

    size_kb = PDF_PATH.stat().st_size // 1024
    print(f"[3/3] Photo HR + ATS   : OK  ->  {PDF_PATH.name} ({size_kb} Ko)")


asyncio.run(build())
