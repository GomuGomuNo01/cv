# Instagram Unlike Cleaner : vidéo de présentation (20 s) ouverte en plein
# écran depuis le titre, le lien "Présentation" et l'image de la carte.
# L'image de la carte devient l'affiche de la vidéo, à la place du GIF et de
# la galerie de captures.
#
# La vidéo est lue depuis la page GitHub du projet : elle y est servie avec
# les requêtes partielles (Range), indispensables à Safari / iOS, ce que le
# service des médias de Django ne fait pas.

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'
VIDEO_URL = 'https://gomugomuno01.github.io/Instagram-Unlike-Cleaner/presentation.mp4'
POSTER = 'projects/instagram-unlike-cleaner-poster.webp'

OLD_IMAGE = 'projects/instagram-unlike-cleaner-demo.gif'
OLD_GALLERY = [
    (1, 'projects/gallery/instagram-unlike-cleaner-01.webp'),
    (2, 'projects/gallery/instagram-unlike-cleaner-02.webp'),
    (3, 'projects/gallery/instagram-unlike-cleaner-03.webp'),
    (4, 'projects/gallery/instagram-unlike-cleaner-04.webp'),
    (5, 'projects/gallery/instagram-unlike-cleaner-05.webp'),
    (6, 'projects/gallery/instagram-unlike-cleaner-06.webp'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url=VIDEO_URL, image=POSTER)
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
        ('core', '0040_project_video_url'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
