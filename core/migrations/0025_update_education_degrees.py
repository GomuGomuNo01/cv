# Simplifie les intitulés des deux mastères (retire le préfixe
# "Informatique - ") suite à la demande du titulaire.
#
# Note : la formulation demandée pour ESIIA contenait deux coquilles
# ("Inteligence Artificiel" au lieu de "Intelligence Artificielle") ;
# l'orthographe correcte est appliquée ici, cohérente avec le reste du site.

from django.db import migrations

UPDATES = [
    ('ESGI Paris', 'Mastère Intelligence Artificielle & Big Data'),
    ('ESIIA Torcy', 'Mastère Intelligence Artificielle et Management de projet numérique'),
]

OLD_VALUES = {
    'ESGI Paris': 'Mastère Informatique - Intelligence Artificielle & Big Data',
    'ESIIA Torcy': 'Mastère Informatique - IA & Management de projet numérique',
}


def apply_new(apps, schema_editor):
    Education = apps.get_model('core', 'Education')
    for school, degree in UPDATES:
        Education.objects.filter(school=school).update(degree=degree)


def revert_old(apps, schema_editor):
    Education = apps.get_model('core', 'Education')
    for school, degree in OLD_VALUES.items():
        Education.objects.filter(school=school).update(degree=degree)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_certification_premiers_pas_cloud'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
