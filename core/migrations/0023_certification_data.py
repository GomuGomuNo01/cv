# Ajoute la certification AWS SimuLearn : Les fondamentaux du cloud,
# obtenue le 30 septembre 2026 (certificat PDF fourni par le titulaire).

from django.db import migrations

CERTIFICATIONS = [
    dict(
        title='AWS SimuLearn : Les fondamentaux du cloud',
        issuer='AWS Training & Certification',
        issue_date='2026-09-30',
        icon_name='workspace_premium',
        certificate_file='certifications/aws-simulearn-fondamentaux-cloud.pdf',
        order=1,
    ),
]


def populate(apps, schema_editor):
    Certification = apps.get_model('core', 'Certification')
    for data in CERTIFICATIONS:
        Certification.objects.get_or_create(title=data['title'], issuer=data['issuer'], defaults=data)


def unpopulate(apps, schema_editor):
    Certification = apps.get_model('core', 'Certification')
    Certification.objects.filter(title__in=[c['title'] for c in CERTIFICATIONS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_certification'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
