# Data migration: populates the portfolio with Cédric Kouadio's real,
# verified profile (experiences, projects, skills) so the site renders
# correctly out of the box without any manual admin entry.

from datetime import date

from django.db import migrations

SKILLS = [
    # (category, name, icon_name, order)
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
]

COMPANIES = [
    dict(
        name='madameb0nplan', location='Paris, France',
        job_title='Stagiaire Data Analyst',
        start_date=date(2026, 1, 1), end_date=date(2026, 6, 30), is_current=False,
        description=(
            "Automatisation de la collecte de données via des scripts Python, "
            "fiabilisation de bases SQL via nettoyage et contrôles qualité, "
            "alimentation de tableaux de bord Power BI restitués quotidiennement à l'équipe."
        ),
    ),
    dict(
        name='IT-CENTREX', location='Abidjan, Côte d’Ivoire',
        job_title='Développeur (Python & IA)',
        start_date=date(2024, 7, 1), end_date=date(2025, 8, 31), is_current=False,
        description=(
            "Conception de modèles de détection d'anomalies (scikit-learn), "
            "développement d'API REST (Java, Python) connectant plusieurs systèmes existants, "
            "fiabilisation de traitements de données répétitifs."
        ),
    ),
    dict(
        name='TASNIM SOLUTION', location='Abidjan, Côte d’Ivoire',
        job_title='Stagiaire Développeur',
        start_date=date(2024, 2, 1), end_date=date(2024, 4, 30), is_current=False,
        description=(
            "Développement d'applications web avec Laravel (MVC, ORM Eloquent) "
            "et d'une application C# d'automatisation."
        ),
    ),
    dict(
        name='Institut Pasteur de Côte d’Ivoire', location='Abidjan, Côte d’Ivoire',
        job_title='Stagiaire Développeur',
        start_date=date(2022, 11, 1), end_date=date(2023, 7, 31), is_current=False,
        description=(
            "Conception et administration de bases de données relationnelles "
            "(MySQL, SQL Server) via modélisation et migration, développement d'une "
            "application interne utilisée par du personnel non technique."
        ),
    ),
]

PROJECTS = [
    dict(
        index_number='01', title='Chatbot RAG - DocAssist', slug='chatbot-rag-docassist',
        short_description=(
            "Répond aux questions posées sur des documents internes en citant toujours "
            "la source, et refuse de répondre plutôt que d'inventer si l'information n'y "
            "figure pas. Tests 100 % automatisés, déployé en production."
        ),
        tech_stack='Python,RAG,FAISS,LangChain,Streamlit',
        github_link='https://github.com/GomuGomuNo01/Chatbot-RAG',
        live_link='https://gomugomuno01-chatbot-rag.hf.space/',
    ),
    dict(
        index_number='02', title='NYC Taxi Data Engineering Pipeline', slug='nyc-taxi-data-engineering',
        short_description=(
            "Transforme 500 000 lignes de données brutes en données fiables et exploitables, "
            "en repérant et documentant 2,3 % de lignes invalides plutôt que de les ignorer."
        ),
        tech_stack='Python,PySpark,Architecture médaillon',
        github_link='https://github.com/GomuGomuNo01/nyc-taxi-data-engineering',
        live_link='',
    ),
    dict(
        index_number='03', title='Maven Toys Analytics (Power BI)', slug='maven-toys-powerbi',
        short_description=(
            "Révèle qu'une enseigne de 50 magasins perd 29 069 $ chaque mois à cause de "
            "ruptures de stock, alors que son chiffre d'affaires progresse. "
            "Analyse de 829 262 ventes."
        ),
        tech_stack='Power BI,DAX,Power Query',
        github_link='https://github.com/GomuGomuNo01/maven-toys-powerbi-analytics',
        live_link='',
    ),
    dict(
        index_number='04', title='SBS Bank', slug='sbs-bank',
        short_description=(
            "Révèle que les clients apportés par des partenaires activent leur compte "
            "2,4 fois moins souvent que les autres, avec 6 recommandations pour y remédier. "
            "Analyse de 1 800 clients et 254 000 opérations."
        ),
        tech_stack='SQL,Python,Statistiques',
        github_link='https://github.com/GomuGomuNo01/Simple-Banking-System-Python',
        live_link='',
    ),
    dict(
        index_number='05', title='Automatisation de Processus', slug='automatisation-de-processus',
        short_description=(
            "Remplace 6 tâches manuelles (surveillance de stock, alertes par email, relevé "
            "des prix concurrents) sans intervention humaine. En service depuis 2 ans."
        ),
        tech_stack='Python,Selenium,Automatisation',
        github_link='https://github.com/GomuGomuNo01/automatisation-de-processus',
        live_link='https://github.com/codespaces/new/GomuGomuNo01/automatisation-de-processus',
    ),
    dict(
        index_number='06', title='Mini-CRM (.NET)', slug='mini-crm-dotnet',
        short_description=(
            "Application de gestion clients et contrats validée par 52 tests automatisés, "
            "avec authentification et gestion des rôles utilisateurs."
        ),
        tech_stack='C#,ASP.NET Core,Entity Framework Core,MySQL',
        github_link='https://github.com/GomuGomuNo01/mini_crm',
        live_link='',
    ),
]


def populate(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Company = apps.get_model('core', 'Company')
    Project = apps.get_model('core', 'Project')

    for category, name, icon_name, order in SKILLS:
        Skill.objects.get_or_create(
            name=name, category=category,
            defaults={'icon_name': icon_name, 'order': order},
        )

    for data in COMPANIES:
        Company.objects.get_or_create(name=data['name'], job_title=data['job_title'], defaults=data)

    for data in PROJECTS:
        Project.objects.get_or_create(slug=data['slug'], defaults=data)


def unpopulate(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Company = apps.get_model('core', 'Company')
    Project = apps.get_model('core', 'Project')

    Skill.objects.filter(name__in=[s[1] for s in SKILLS]).delete()
    Company.objects.filter(name__in=[c['name'] for c in COMPANIES]).delete()
    Project.objects.filter(slug__in=[p['slug'] for p in PROJECTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_update_categories_and_image'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
