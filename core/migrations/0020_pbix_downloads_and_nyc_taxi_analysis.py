# 1. Ajoute le projet NYC Taxi Analyse des Revenus (dépôt
#    nyc-taxi-analyse-revenus), placé juste après le pipeline NYC Taxi.
# 2. Ajoute un lien de téléchargement du rapport Power BI (.pbix) sur les
#    4 projets qui en publient un dans les releases GitHub. Les liens
#    "releases/latest/download/..." sont ceux déjà utilisés dans les README.

from django.db import migrations

PBIX_LABEL = '.pbix avec données'
BASE = 'https://github.com/GomuGomuNo01'

DOWNLOADS = {
    'nyc-taxi-analyse-revenus': f'{BASE}/nyc-taxi-analyse-revenus/releases/latest/download/NYC_Taxi_Dashboard.pbix',
    'contoso-sales-powerbi': f'{BASE}/contoso-sales-powerbi/releases/latest/download/Contoso-Ventes.pbix',
    'maven-toys-powerbi': f'{BASE}/maven-toys-powerbi-analytics/releases/latest/download/MavenToys_Pilotage.pbix',
    'sbs-bank': f'{BASE}/Simple-Banking-System-Python/releases/latest/download/SBS_Bank.pbix',
}

NEW_PROJECT = dict(
    index_number='04', title='NYC Taxi Analyse des Revenus (Power BI)', slug='nyc-taxi-analyse-revenus',
    short_description=(
        "Analyse de 7,7 millions de courses de taxis new-yorkais pour déterminer où et quand "
        "positionner les chauffeurs afin de maximiser leur revenu. Révèle que les aéroports "
        "représentent 6 % des courses mais 21 % du chiffre d'affaires. Dashboard Power BI de "
        "5 pages avec recommandations."
    ),
    tech_stack='Power BI,DAX,SQL,PySpark',
    github_link=f'{BASE}/nyc-taxi-analyse-revenus',
    live_link='',
    image='projects/nyc-taxi-analyse-demo.gif',
    is_featured=True,
    in_progress=False,
)

GALLERY = [
    (1, 'projects/gallery/nyc-taxi-analyse-01.webp'),
    (2, 'projects/gallery/nyc-taxi-analyse-02.webp'),
    (3, 'projects/gallery/nyc-taxi-analyse-03.webp'),
    (4, 'projects/gallery/nyc-taxi-analyse-04.webp'),
    (5, 'projects/gallery/nyc-taxi-analyse-05.webp'),
]

NEW_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('hotel-management-system', '02'),
    ('nyc-taxi-data-engineering', '03'),
    ('nyc-taxi-analyse-revenus', '04'),
    ('maven-toys-powerbi', '05'),
    ('contoso-sales-powerbi', '06'),
    ('sbs-bank', '07'),
    ('telco-churn-prediction', '08'),
    ('automatisation-de-processus', '09'),
    ('sales-report-automation', '10'),
    ('mini-crm-dotnet', '11'),
    ('api-rest-jwt', '12'),
    ('hospital', '13'),
]

OLD_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('hotel-management-system', '02'),
    ('nyc-taxi-data-engineering', '03'),
    ('maven-toys-powerbi', '04'),
    ('contoso-sales-powerbi', '05'),
    ('sbs-bank', '06'),
    ('telco-churn-prediction', '07'),
    ('automatisation-de-processus', '08'),
    ('sales-report-automation', '09'),
    ('mini-crm-dotnet', '10'),
    ('api-rest-jwt', '11'),
    ('hospital', '12'),
]


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    project, _ = Project.objects.get_or_create(slug=NEW_PROJECT['slug'], defaults=NEW_PROJECT)
    for order, path in GALLERY:
        ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})

    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)

    for slug, url in DOWNLOADS.items():
        Project.objects.filter(slug=slug).update(download_link=url, download_label=PBIX_LABEL)


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=NEW_PROJECT['slug']).delete()
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)
    Project.objects.filter(slug__in=DOWNLOADS.keys()).update(download_link='', download_label='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_project_download_link'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
