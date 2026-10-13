# Technologies des projets et des compétences réalignées sur le contenu réel
# des dépôts GitHub (dépendances, imports, manifestes), relevé le 13/10/2026.
# Corrections notables :
#   - Sales Report : le PDF est généré avec fpdf2, pas ReportLab ;
#   - Mini-CRM : le projet cible .NET 10 (pas ASP.NET Core 8), en MVC ;
#   - Automatisation : Playwright n'y sert qu'à un script de CI, le cœur
#     repose sur Selenium, pandas, openpyxl et Streamlit ;
#   - SBS Bank, Telco : méthodes (RFM, tests statistiques, "Machine
#     Learning") remplacées par les outils effectivement utilisés.

from django.db import migrations

PROJECTS = {
    # slug: (nouveau, ancien)
    'chatbot-rag-docassist': ('Python,LangChain,FAISS,API Claude,FastAPI,Docker', 'Python,LangChain,FAISS,FastAPI'),
    'instagram-unlike-cleaner': ('Python,Playwright,FastAPI,SQLModel,React,TypeScript', 'Python,Playwright,FastAPI,React,TypeScript'),
    'sales-report-automation': ('Python,pandas,Matplotlib,fpdf2,Streamlit,pytest', 'Python,pandas,ReportLab,pytest'),
    'maven-toys-powerbi': ('Power BI,DAX,Power Query,Python,pandas', 'Power BI,DAX,Power Query,Python'),
    'contoso-sales-powerbi': ('Power BI,DAX,Power Query,Python,pandas', 'Power BI,DAX,Power Query,Python'),
    'nyc-taxi-data-engineering': ('Python,PySpark,DuckDB,Parquet,Power BI,DAX', 'Python,PySpark,SQL,Power BI,DAX'),
    'sbs-bank': ('Python,MySQL,pandas,SciPy,Power BI,DAX', 'Python,SQL,Segmentation RFM,Tests statistiques'),
    'telco-churn-prediction': ('Python,scikit-learn,XGBoost,statsmodels,Streamlit', 'Python,scikit-learn,Machine Learning'),
    'automatisation-de-processus': ('Python,Selenium,pandas,openpyxl,Streamlit', 'Python,Selenium,Playwright,openpyxl'),
    'hotel-management-system': ('Laravel,PHP,React,MySQL,Laravel Reverb,Docker', 'Laravel,React,MySQL,WebSocket'),
    'api-rest-jwt': ('Java,Spring Boot,Spring Security,JWT,MySQL,JUnit', 'Java,Spring Boot,Spring Security,JUnit,Swagger'),
    'mini-crm-dotnet': ('C#,ASP.NET Core MVC,Entity Framework Core,MySQL,xUnit', 'C#,ASP.NET Core 8,Entity Framework Core,MySQL'),
    'hospital': ('Laravel,PHP,Blade,Tailwind CSS,MySQL', 'Laravel,PHP,Blade,MySQL'),
}

SKILLS = {
    # (catégorie, ordre): (nouveau, ancien)
    ('data', 3): ('Power BI (DAX, Power Query, format PBIP)', 'Power BI (DAX, Power Query)'),
    ('data', 4): ('PySpark / architecture médaillon (Parquet)', 'PySpark / architecture médaillon'),
    ('dev', 4): ('C# / ASP.NET Core MVC (Entity Framework Core, Identity)', 'C# / ASP.NET Core (Entity Framework Core)'),
    ('outils', 4): ('Tests automatisés (pytest, JUnit, PHPUnit, xUnit, Vitest, Playwright)',
                    'Tests automatisés (pytest, PHPUnit, xUnit, Vitest, Playwright)'),
    ('outils', 5): ('Cloud (AWS fondamentaux, Cloudflare R2, Render, GitHub Pages)',
                    'Cloud (AWS fondamentaux, Render, GitHub Pages)'),
}


def _apply(apps, index):
    Project = apps.get_model('core', 'Project')
    Skill = apps.get_model('core', 'Skill')
    for slug, values in PROJECTS.items():
        Project.objects.filter(slug=slug).update(tech_stack=values[index])
    for (category, order), values in SKILLS.items():
        Skill.objects.filter(category=category, order=order).update(name=values[index])


def apply_new(apps, schema_editor):
    _apply(apps, 0)


def revert_old(apps, schema_editor):
    _apply(apps, 1)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_mini_crm_text_and_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
