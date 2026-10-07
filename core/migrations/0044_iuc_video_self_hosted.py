# La vidéo de présentation d'IUC était lue depuis la page GitHub du projet,
# qui ne répond plus (404 : GitHub Pages désactivé sur le dépôt). Elle est
# désormais hébergée dans le portfolio comme fichier statique, servi par
# WhiteNoise avec les requêtes partielles (Range) nécessaires à Safari / iOS.

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'
NEW_VIDEO = 'core/videos/instagram-unlike-cleaner-presentation.mp4'
OLD_VIDEO = 'https://gomugomuno01.github.io/Instagram-Unlike-Cleaner/presentation.mp4'


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(video_url=NEW_VIDEO)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(video_url=OLD_VIDEO)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_project_video_static'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
