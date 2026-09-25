# Marque le Système de Gestion Hôtelière comme "en cours" et le repositionne
# en 2e position (juste après Chatbot RAG), en décalant les projets suivants.

from django.db import migrations

NEW_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('hotel-management-system', '02'),
    ('nyc-taxi-data-engineering', '03'),
    ('maven-toys-powerbi', '04'),
    ('contoso-sales-powerbi', '05'),
    ('sbs-bank', '06'),
    ('telco-churn-prediction', '07'),
    ('automatisation-de-processus', '08'),
    ('sales-report-automation', '09'),
    ('mini-crm-dotnet', '10'),
    ('api-rest-jwt', '11'),
    ('hospital', '12'),
]


def apply_order(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)
    Project.objects.filter(slug='hotel-management-system').update(in_progress=True)


def revert_order(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    # Ancien ordre : hotel-management-system était en 12e position, "terminé".
    OLD_ORDER = [
        ('chatbot-rag-docassist', '01'),
        ('nyc-taxi-data-engineering', '02'),
        ('maven-toys-powerbi', '03'),
        ('contoso-sales-powerbi', '04'),
        ('sbs-bank', '05'),
        ('telco-churn-prediction', '06'),
        ('automatisation-de-processus', '07'),
        ('sales-report-automation', '08'),
        ('mini-crm-dotnet', '09'),
        ('api-rest-jwt', '10'),
        ('hospital', '11'),
        ('hotel-management-system', '12'),
    ]
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)
    Project.objects.filter(slug='hotel-management-system').update(in_progress=False)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_hotel_management_system'),
    ]

    operations = [
        migrations.RunPython(apply_order, revert_order),
    ]
