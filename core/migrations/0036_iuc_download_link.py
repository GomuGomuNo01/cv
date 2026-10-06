# Ajoute le lien de téléchargement de l'installeur Windows (IUC-Setup.exe)
# sur la carte Instagram Unlike Cleaner, à côté du lien de démo.

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'
DOWNLOAD_LINK = 'https://github.com/GomuGomuNo01/Instagram-Unlike-Cleaner/releases/latest/download/IUC-Setup.exe'
DOWNLOAD_LABEL = '.exe pour Windows'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(download_link=DOWNLOAD_LINK, download_label=DOWNLOAD_LABEL)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(download_link='', download_label='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_add_instagram_unlike_cleaner'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
