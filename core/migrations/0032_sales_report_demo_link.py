# Ajoute le lien de démo Google Colab pour Sales Report Automation.

from django.db import migrations

SLUG = 'sales-report-automation'
NEW_LIVE_LINK = 'https://colab.research.google.com/github/GomuGomuNo01/sales-report-automation/blob/main/demo_colab.ipynb'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link=NEW_LIVE_LINK)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_link='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_company_tasks'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
