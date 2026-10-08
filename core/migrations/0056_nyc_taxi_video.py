# NYC Taxi reprend la présentation de DocAssist, IUC, Sales Report, Maven
# Toys et Contoso : vidéo de présentation (40 s) ouverte en plein écran
# depuis le titre, le lien "Présentation" et l'image de la carte ; l'image
# devient l'affiche de la vidéo, à la place du GIF et de la galerie. Le
# bouton de téléchargement du .pbix est conservé.
# Vidéo et affiche reprises du dépôt nyc-taxi-analyse-revenus
# (assets/video/), vidéo servie comme fichier statique par WhiteNoise.
# Position inchangée : 06, déjà juste après Contoso Sales Analytics.

from django.db import migrations

SLUG = 'nyc-taxi-data-engineering'
VIDEO = 'core/videos/nyc-taxi-presentation.mp4'
POSTER = 'projects/nyc-taxi-poster.webp'
OLD_IMAGE = 'projects/nyc-taxi-analyse-demo.gif'
OLD_GALLERY = [
    (1, 'projects/gallery/nyc-taxi-analyse-01.webp'),
    (2, 'projects/gallery/nyc-taxi-analyse-02.webp'),
    (3, 'projects/gallery/nyc-taxi-analyse-03.webp'),
    (4, 'projects/gallery/nyc-taxi-analyse-04.webp'),
    (5, 'projects/gallery/nyc-taxi-analyse-05.webp'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url=VIDEO, image=POSTER)
    ProjectImage.objects.filter(project__slug=SLUG).delete()


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url='', image=OLD_IMAGE)
    project = Project.objects.filter(slug=SLUG).first()
    if project:
        for order, path in OLD_GALLERY:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_contoso_maven_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
