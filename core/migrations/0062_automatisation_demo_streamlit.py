# Automatisation de processus : le lien Démo pointe vers l'application
# Streamlit publiée, à la place de l'ouverture d'un Codespace.

from django.db import migrations

SLUG = 'automatisation-de-processus'
NEW_LINK = 'https://automatisation-de-processus-cedric.streamlit.app/'
OLD_LINK = 'https://github.com/codespaces/new/GomuGomuNo01/automatisation-de-processus'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link=NEW_LINK)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link=OLD_LINK)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_automatisation_text_and_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
