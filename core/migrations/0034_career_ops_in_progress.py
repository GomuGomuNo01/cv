# Marque Career-Ops comme en cours et lui applique l'illustration de
# maintenance générique, en cohérence avec les autres projets en cours
# (Système de Gestion Hôtelière, Telco Churn Prediction).

from django.db import migrations

SLUG = 'career-ops'
MAINTENANCE_IMAGE = 'projects/maintenance-generic.svg'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(in_progress=True, image=MAINTENANCE_IMAGE)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(in_progress=False, image='')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_add_career_ops'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
