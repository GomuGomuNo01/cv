# 1. Le pipeline NYC Taxi Data Engineering est terminé (release v1.0 sur le
#    dépôt) : retire le badge "en cours".
# 2. Les projets encore en cours de développement (hotel-management-system,
#    telco-churn-prediction) utilisent désormais une illustration générique
#    "en maintenance" plutôt qu'une maquette de l'interface finale.

from django.db import migrations

MAINTENANCE_IMAGE = 'projects/maintenance-generic.svg'

MAINTENANCE_PROJECTS = {
    'hotel-management-system': 'projects/hotel-management-generic.svg',
    'telco-churn-prediction': 'projects/telco-churn-generic.svg',
}


def apply_changes(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug='nyc-taxi-data-engineering').update(in_progress=False)
    for slug in MAINTENANCE_PROJECTS:
        Project.objects.filter(slug=slug).update(image=MAINTENANCE_IMAGE)


def revert_changes(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug='nyc-taxi-data-engineering').update(in_progress=True)
    for slug, old_image in MAINTENANCE_PROJECTS.items():
        Project.objects.filter(slug=slug).update(image=old_image)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_update_companies_full_history'),
    ]

    operations = [
        migrations.RunPython(apply_changes, revert_changes),
    ]
