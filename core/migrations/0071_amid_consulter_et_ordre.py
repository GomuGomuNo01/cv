# Site AMID 2026 : le lien externe s'intitule "Consulter" (et non "Démo", car
# c'est un site d'événement et non une application à tester), et le projet
# passe juste après Système de Gestion Hôtelière dans la catégorie Développement.
#
# Ordre Développement : Hôtel (09), AMID (10), API REST JWT (11), Mini-CRM (12).

from django.db import migrations

SLUG = 'site-amid-2026'

NEW_ORDER = [
    ('hotel-management-system', '09'),
    ('site-amid-2026', '10'),
    ('api-rest-jwt', '11'),
    ('mini-crm-dotnet', '12'),
]

OLD_ORDER = [
    ('hotel-management-system', '09'),
    ('api-rest-jwt', '10'),
    ('mini-crm-dotnet', '11'),
    ('site-amid-2026', '12'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_label='Consulter')
    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(live_label='')
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_project_live_label'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
