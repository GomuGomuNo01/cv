# Aligne la description d'Instagram Unlike Cleaner sur le dépôt (v1.2.0) :
# le nombre de tests passe de 283 à 288.

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'

NEW_DESCRIPTION = (
    "Une personne veut effacer des années de likes Instagram sans confier son mot de "
    "passe ni ses données. IUC, outil 100 % local, cible les likes avec le filtre "
    "d'Instagram, les liste pour validation puis les retire par lots prudents : 1 493 "
    "likes recensés en 14 min sur un vrai compte, et 288 tests prouvent qu'aucun "
    "identifiant n'est lu ni conservé."
)

OLD_DESCRIPTION = NEW_DESCRIPTION.replace('288 tests', '283 tests')


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_iuc_download_link'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
