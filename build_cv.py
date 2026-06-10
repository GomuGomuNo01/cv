"""
build_cv.py – Convertit CV_Kouadio_Cedric.html en PDF via Chromium (Playwright)
"""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

HTML_PATH = Path(__file__).parent / "CV_Kouadio_Cedric.html"
PDF_PATH  = Path(__file__).parent / "CV_Kouadio_Cedric.pdf"


async def build():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Charger le fichier HTML local
        await page.goto(HTML_PATH.as_uri(), wait_until="networkidle")

        # Générer le PDF A4 sans marges, avec fonds colorés
        await page.pdf(
            path=str(PDF_PATH),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )

        await browser.close()

    print(f"PDF généré : {PDF_PATH}")
    print(f"Taille     : {PDF_PATH.stat().st_size // 1024} Ko")


asyncio.run(build())
