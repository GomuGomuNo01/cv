# Pour les projets dont le dépôt GitHub ne contient aucune image (NYC
# Taxi, Telco Churn, Mini-CRM), utilise une illustration générique
# vectorielle (SVG, dessinée pour ce portfolio, cohérente avec sa charte
# graphique) plutôt que de laisser un simple pictogramme de remplacement.
# Ce ne sont pas des captures de l'application, juste une illustration
# thématique.

from django.db import migrations

GENERIC_IMAGES = {
    'nyc-taxi-data-engineering': 'projects/nyc-taxi-generic.svg',
    'telco-churn-prediction': 'projects/telco-churn-generic.svg',
    'mini-crm-dotnet': 'projects/mini-crm-generic.svg',
}


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, path in GENERIC_IMAGES.items():
        Project.objects.filter(slug=slug).update(image=path)


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=GENERIC_IMAGES.keys()).update(image=None)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_api_rest_jwt_images'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
