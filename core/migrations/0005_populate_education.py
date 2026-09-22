from datetime import date

from django.db import migrations

EDUCATIONS = [
    dict(
        school='ESGI Paris',
        degree='Mastère Informatique - Intelligence Artificielle & Big Data',
        location='Paris, France',
        start_date=date(2026, 9, 1), end_date=None, is_current=True,
    ),
    dict(
        school='ESIIA Torcy',
        degree='Mastère Informatique - IA & Management de projet numérique',
        location='Torcy, France',
        start_date=date(2025, 9, 1), end_date=date(2026, 6, 30), is_current=False,
    ),
    dict(
        school='PIGIER Côte d’Ivoire',
        degree='Licence Professionnelle Réseaux & Génie Logiciel, BTS Développement d’Applications',
        location='Abidjan, Côte d’Ivoire',
        start_date=date(2021, 9, 1), end_date=date(2024, 6, 30), is_current=False,
    ),
]


def populate(apps, schema_editor):
    Education = apps.get_model('core', 'Education')
    for data in EDUCATIONS:
        Education.objects.get_or_create(school=data['school'], degree=data['degree'], defaults=data)


def unpopulate(apps, schema_editor):
    Education = apps.get_model('core', 'Education')
    Education.objects.filter(school__in=[e['school'] for e in EDUCATIONS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_education'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
