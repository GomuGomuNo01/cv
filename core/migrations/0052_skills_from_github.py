# Met à jour la section Compétences à partir des dépôts GitHub du titulaire
# (fichiers de dépendances, workflows, README), audit du 08/10/2026.
#
# Preuves principales :
#  - Data : pandas/NumPy/Matplotlib/Seaborn (sales-report, SBS, NYC...),
#    DuckDB + PySpark (nyc-taxi), XGBoost/statsmodels/scikit-learn (telco),
#    khi-deux/RFM/SciPy (SBS), DAX/Power Query (Maven, Contoso, NYC, SBS).
#  - IA : LangChain/FAISS/sentence-transformers + langchain-anthropic
#    (Chatbot-RAG), CLAUDE.md dans 5 dépôts, Playwright (IUC),
#    Selenium/schedule (automatisation), fpdf2/openpyxl (sales-report),
#    Streamlit (sales-report, telco), Hugging Face Spaces (Chatbot-RAG).
#  - Dev : FastAPI/Pydantic/SQLModel (Chatbot, IUC), Spring Boot/Security/JJWT
#    (api-rest-jwt), Laravel/Sanctum/Reverb (hotel, Hospital...),
#    ASP.NET Core/EF Core (mini_crm), React/TypeScript/Vite/Tailwind (hotel,
#    IUC), Flutter/Dart (sauveTonPlatFront).
#  - Outils : GitHub Actions (CI dans 4 dépôts), Docker/Compose,
#    pytest/PHPUnit/xUnit/Vitest/Playwright, MySQL/SQLite.
# PostgreSQL, SQL Server et MCP ne figurent dans aucun dépôt : conservés car
# issus du CV et de l'expérience professionnelle (déjà validés).

from django.db import migrations

# (catégorie, nom, icône, ordre)
NEW_SKILLS = [
    ('data', 'Python (pandas, NumPy, Matplotlib, Seaborn)', 'code', 1),
    ('data', 'SQL avancé (CTE, fonctions fenêtrées, DuckDB)', 'database', 2),
    ('data', 'Power BI (DAX, Power Query)', 'bar_chart', 3),
    ('data', 'PySpark / architecture médaillon', 'hub', 4),
    ('data', 'Machine learning (scikit-learn, XGBoost, statsmodels)', 'model_training', 5),
    ('data', 'Statistiques et segmentation (khi-deux, RFM, SciPy)', 'functions', 6),

    ('ia', 'RAG (LangChain, FAISS, sentence-transformers)', 'hub', 1),
    ('ia', 'API Claude (Anthropic), prompt engineering', 'psychology', 2),
    ('ia', 'Agents IA (Claude Code, serveurs MCP)', 'smart_toy', 3),
    ('ia', 'Automatisation navigateur (Playwright, Selenium)', 'bolt', 4),
    ('ia', 'Rapports automatisés (fpdf2, openpyxl, tâches planifiées)', 'description', 5),
    ('ia', 'Déploiement (Streamlit, Hugging Face Spaces)', 'rocket_launch', 6),

    ('dev', 'Python / FastAPI (Pydantic, SQLModel)', 'api', 1),
    ('dev', 'Java / Spring Boot (Spring Security, JWT)', 'code', 2),
    ('dev', 'PHP / Laravel (Sanctum, Reverb)', 'code', 3),
    ('dev', 'C# / ASP.NET Core (Entity Framework Core)', 'code', 4),
    ('dev', 'JavaScript / TypeScript / React (Vite, Tailwind CSS)', 'web', 5),
    ('dev', 'Flutter / Dart (mobile)', 'smartphone', 6),

    ('outils', 'Git / GitHub Actions (CI/CD)', 'code', 1),
    ('outils', 'Docker / Docker Compose', 'inventory_2', 2),
    ('outils', 'MySQL / PostgreSQL / SQL Server / SQLite', 'storage', 3),
    ('outils', 'Tests automatisés (pytest, PHPUnit, xUnit, Vitest, Playwright)', 'task_alt', 4),
    ('outils', 'Cloud (AWS fondamentaux, Render, GitHub Pages)', 'cloud', 5),
    ('outils', 'Excel avancé', 'table_chart', 6),
]

OLD_SKILLS = [
    ('data', 'Python (pandas, numpy, scikit-learn)', 'code', 1),
    ('data', 'SQL avancé (CTE, fonctions fenêtrées)', 'database', 2),
    ('data', 'Power BI (DAX, Power Query)', 'bar_chart', 3),
    ('data', 'PySpark / architecture médaillon', 'hub', 4),
    ('data', 'Statistiques appliquées (test du khi-deux)', 'functions', 5),
    ('ia', 'Agents IA (Claude Code, serveurs MCP)', 'smart_toy', 1),
    ('ia', 'RAG (LangChain, FAISS)', 'hub', 2),
    ('ia', 'Prompt engineering', 'psychology', 3),
    ('ia', 'Automatisation (Selenium, scripts Python)', 'bolt', 4),
    ('ia', 'Déploiement Streamlit', 'rocket_launch', 5),
    ('dev', 'Java / Spring Boot', 'code', 1),
    ('dev', 'PHP / Laravel', 'code', 2),
    ('dev', 'C# / ASP.NET Core', 'code', 3),
    ('dev', 'JavaScript / HTML / CSS', 'code', 4),
    ('dev', 'API REST (FastAPI, JWT)', 'api', 5),
    ('outils', 'Git / GitHub', 'code', 1),
    ('outils', 'Docker', 'inventory_2', 2),
    ('outils', 'MySQL / PostgreSQL / SQL Server', 'storage', 3),
    ('outils', 'Excel avancé', 'table_chart', 4),
    ('outils', 'Tests automatisés (pytest, xUnit)', 'task_alt', 5),
    ('outils', 'Cloud (AWS - fondamentaux)', 'cloud', 6),
]


def replace_with(skills):
    def run(apps, schema_editor):
        Skill = apps.get_model('core', 'Skill')
        Skill.objects.all().delete()
        Skill.objects.bulk_create([
            Skill(category=c, name=n, icon_name=i, order=o) for c, n, i, o in skills
        ])
    return run


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_sales_report_streamlit_demo'),
    ]

    operations = [
        migrations.RunPython(replace_with(NEW_SKILLS), replace_with(OLD_SKILLS)),
    ]
