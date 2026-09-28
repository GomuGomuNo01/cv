# Le dépôt GitHub nyc-taxi-data-engineering a été renommé en
# nyc-taxi-analyse-revenus : c'est le même projet que la carte
# "NYC Taxi Data Engineering Pipeline". La migration 0020 avait créé une
# carte en double, elle est supprimée ici et ses éléments (aperçu animé,
# captures du dashboard, téléchargement du .pbix, description à jour) sont
# rattachés à la carte existante.

from django.db import migrations

SLUG = 'nyc-taxi-data-engineering'
DUPLICATE_SLUG = 'nyc-taxi-analyse-revenus'
REPO = 'https://github.com/GomuGomuNo01/nyc-taxi-analyse-revenus'

NEW_VALUES = dict(
    short_description=(
        "Analyse de 7,7 millions de courses de taxis new-yorkais pour déterminer où et quand "
        "positionner les chauffeurs afin de maximiser leur revenu. Les données sont nettoyées "
        "et chaque exclusion est documentée (97 % des données restent exploitables). Révèle que "
        "les aéroports représentent 6 % des courses mais 21 % du chiffre d'affaires. Dashboard "
        "Power BI de 5 pages avec recommandations."
    ),
    tech_stack='PySpark,SQL,Power BI,DAX,Architecture médaillon',
    github_link=REPO,
    image='projects/nyc-taxi-analyse-demo.gif',
    download_link=f'{REPO}/releases/latest/download/NYC_Taxi_Dashboard.pbix',
    download_label='.pbix avec données',
)

OLD_VALUES = dict(
    short_description=(
        "Nettoie et organise 500 000 trajets de taxis new-yorkais bruts et incomplets pour les "
        "rendre exploitables dans des analyses. Repère et documente chaque donnée invalide "
        "(2,3 % du total) au lieu de la supprimer en silence, pour que les résultats finaux "
        "restent fiables."
    ),
    tech_stack='Python,PySpark,Architecture médaillon',
    github_link='https://github.com/GomuGomuNo01/nyc-taxi-data-engineering',
    image='projects/nyc-taxi-generic.svg',
    download_link='',
    download_label='',
)

GALLERY = [
    (1, 'projects/gallery/nyc-taxi-analyse-01.webp'),
    (2, 'projects/gallery/nyc-taxi-analyse-02.webp'),
    (3, 'projects/gallery/nyc-taxi-analyse-03.webp'),
    (4, 'projects/gallery/nyc-taxi-analyse-04.webp'),
    (5, 'projects/gallery/nyc-taxi-analyse-05.webp'),
]

ORDER = [
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


def merge(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    Project.objects.filter(slug=DUPLICATE_SLUG).delete()

    project = Project.objects.get(slug=SLUG)
    for field, value in NEW_VALUES.items():
        setattr(project, field, value)
    project.save()

    for order, path in GALLERY:
        ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})

    for slug, index in ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


def unmerge(apps, schema_editor):
    # Restaure la carte d'origine (sans recréer le doublon de la 0020).
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(**OLD_VALUES)
    ProjectImage.objects.filter(project__slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_pbix_downloads_and_nyc_taxi_analysis'),
    ]

    operations = [
        migrations.RunPython(merge, unmerge),
    ]
