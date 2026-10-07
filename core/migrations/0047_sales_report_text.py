# Sales Report Automation : nouveau texte fourni par le titulaire.

from django.db import migrations

SLUG = 'sales-report-automation'

NEW_DESCRIPTION = (
    "Fini les heures de préparation manuelle : ce pipeline transforme un CSV en rapport PDF "
    "complet en 7 secondes, calcule automatiquement les KPI et sécurise le résultat grâce "
    "à 50+ tests automatisés."
)

OLD_DESCRIPTION = (
    "Préparer un rapport commercial à la main prend plusieurs heures et augmente le "
    "risque d'erreur. Ce pipeline transforme un fichier CSV brut en un rapport PDF de "
    "six pages en sept secondes, calcule automatiquement les indicateurs clés et "
    "s'appuie sur plus de 50 tests automatisés pour garantir la fiabilité du résultat."
)


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_remove_career_ops'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
