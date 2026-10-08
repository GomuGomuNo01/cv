# Sales Report Automation : le lien "Démo" pointe désormais vers
# l'application Streamlit (publique) au lieu du notebook Colab.

from django.db import migrations

SLUG = 'sales-report-automation'
NEW_LIVE_LINK = 'https://sales-report-automation-cedric.streamlit.app/'
OLD_LIVE_LINK = 'https://colab.research.google.com/github/GomuGomuNo01/sales-report-automation/blob/main/demo_colab.ipynb'


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(live_link=NEW_LIVE_LINK)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(live_link=OLD_LIVE_LINK)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_hotel_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
