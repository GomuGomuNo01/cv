# Maven Toys Analytics reprend la présentation de DocAssist, IUC et Sales
# Report : vidéo de présentation (40 s) ouverte en plein écran depuis le
# titre, le lien "Présentation" et l'image de la carte ; l'image devient
# l'affiche de la vidéo, à la place du GIF et de la galerie. Le bouton de
# téléchargement du .pbix est conservé.
# Vidéo et affiche reprises du dépôt maven-toys-powerbi-analytics
# (assets/video/), vidéo servie comme fichier statique par WhiteNoise.
#
# Maven Toys passe juste après Sales Report Automation (04).

from django.db import migrations

SLUG = 'maven-toys-powerbi'
VIDEO = 'core/videos/maven-toys-powerbi-presentation.mp4'
POSTER = 'projects/maven-toys-powerbi-poster.webp'
OLD_IMAGE = 'projects/maven-toys-demo.gif'
OLD_GALLERY = [
    (0, 'projects/maven-toys-powerbi.webp'),
    (2, 'projects/gallery/maven-toys-02.webp'),
    (3, 'projects/gallery/maven-toys-03.webp'),
    (4, 'projects/gallery/maven-toys-04.webp'),
]

NEW_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('instagram-unlike-cleaner', '02'),
    ('sales-report-automation', '03'),
    ('maven-toys-powerbi', '04'),
    ('nyc-taxi-data-engineering', '05'),
    ('contoso-sales-powerbi', '06'),
    ('sbs-bank', '07'),
    ('telco-churn-prediction', '08'),
    ('automatisation-de-processus', '09'),
]

OLD_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('instagram-unlike-cleaner', '02'),
    ('sales-report-automation', '03'),
    ('nyc-taxi-data-engineering', '04'),
    ('maven-toys-powerbi', '05'),
    ('contoso-sales-powerbi', '06'),
    ('sbs-bank', '07'),
    ('telco-churn-prediction', '08'),
    ('automatisation-de-processus', '09'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url=VIDEO, image=POSTER)
    ProjectImage.objects.filter(project__slug=SLUG).delete()
    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url='', image=OLD_IMAGE)
    project = Project.objects.filter(slug=SLUG).first()
    if project:
        for order, path in OLD_GALLERY:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_skills_from_github'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
