# Retour des liens vers le code : chaque carte projet affiche un lien
# "Code" vers son dépôt GitHub. Instagram Unlike Cleaner était le seul
# projet sans lien de dépôt, ajouté ici (dépôt public).

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'
REPO = 'https://github.com/GomuGomuNo01/Instagram-Unlike-Cleaner'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(github_link=REPO)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(github_link='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_hotel_management_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
