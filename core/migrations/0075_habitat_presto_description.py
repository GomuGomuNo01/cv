# Nouvelle description du projet Suivi des demandes Habitat Presto (texte fourni par le titulaire).

from django.db import migrations

SLUG = 'monthimmo-habitat-presto'

NEW = (
    "Le pôle travaux d'une entreprise reçoit des demandes clients par email, qu'il faut "
    "recopier à la main sous peine de les oublier. Cet outil lit chaque demande avec l'IA, "
    "la range dans un tableau de suivi sans créer de doublon et prévient le conducteur de "
    "travaux par email, même quand une demande est incomplète ou que le service de lecture "
    "tombe en panne. Plus de vingt scénarios testés, sur des données fictives."
)
OLD = (
    "Le pôle travaux d'une entreprise reçoit des demandes clients par email, qu'il faut "
    "recopier à la main sous peine de les oublier. Un workflow n8n lit chaque demande avec "
    "Claude Haiku, la range dans un tableau Airtable sans doublon et alerte le conducteur "
    "de travaux par Gmail. Il gère les demandes incomplètes et les pannes du service de "
    "lecture. Plus de vingt scénarios sont testés, sur des données fictives."
)


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=NEW)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=OLD)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_add_monthimmo_habitat_presto'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
