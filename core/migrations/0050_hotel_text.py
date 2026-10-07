# Hotel Management System : nouveau texte fourni par le titulaire.

from django.db import migrations

SLUG = 'hotel-management-system'

NEW_DESCRIPTION = (
    "Une plateforme de gestion hôtelière qui centralise réservations, paiements, "
    "arrivées, départs et réclamations pour éviter les erreurs et les conflits de "
    "données. Les informations sont synchronisées instantanément, garantissant une "
    "gestion fluide et fiable des séjours."
)

OLD_DESCRIPTION = (
    "Un hôtel doit gérer les réservations, les paiements, les arrivées, les départs et "
    "les réclamations sans créer de conflits entre les informations. Cette application "
    "centralise le cycle de vie des séjours, tandis que les mises à jour sont "
    "immédiatement visibles grâce à la communication en temps réel entre le serveur et "
    "l'interface."
)


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_reorder_featured_first'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
