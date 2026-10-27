# Suivi des demandes Habitat Presto : lien "Code" vers le dépôt GitHub du
# projet (cas pratique Month'immo), affiché dans la ligne d'actions de la
# carte. Ce projet n'a ni démo en ligne ni vidéo : le dépôt est ce qu'on peut
# consulter. Les autres projets gardent uniquement Démo / Présentation.

from django.db import migrations

SLUG = 'monthimmo-habitat-presto'
REPO = 'https://github.com/GomuGomuNo01/monthimmo-cas-pratique'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link=REPO, live_label='Code')


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link='', live_label='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_habitat_presto_description'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
