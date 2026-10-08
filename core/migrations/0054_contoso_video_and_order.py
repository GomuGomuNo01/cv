# Contoso Sales Analytics reprend la présentation de DocAssist, IUC, Sales
# Report et Maven Toys : vidéo de présentation (40 s) ouverte en plein écran
# depuis le titre, le lien "Présentation" et l'image de la carte ; l'image
# devient l'affiche de la vidéo, à la place du GIF et de la galerie. Le
# bouton de téléchargement du .pbix est conservé.
# Vidéo et affiche reprises du dépôt contoso-sales-powerbi (assets/video/),
# vidéo servie comme fichier statique par WhiteNoise.
#
# Contoso passe juste après Maven Toys Analytics (05).

from django.db import migrations

SLUG = 'contoso-sales-powerbi'
VIDEO = 'core/videos/contoso-sales-powerbi-presentation.mp4'
POSTER = 'projects/contoso-sales-powerbi-poster.webp'
OLD_IMAGE = 'projects/contoso-demo.gif'
OLD_GALLERY = [
    (0, 'projects/contoso-sales-powerbi.webp'),
    (2, 'projects/gallery/contoso-02.webp'),
    (3, 'projects/gallery/contoso-03.webp'),
    (4, 'projects/gallery/contoso-04.webp'),
]

NEW_ORDER = [
    ('contoso-sales-powerbi', '05'),
    ('nyc-taxi-data-engineering', '06'),
]

OLD_ORDER = [
    ('nyc-taxi-data-engineering', '05'),
    ('contoso-sales-powerbi', '06'),
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
        ('core', '0053_maven_video_and_order'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
