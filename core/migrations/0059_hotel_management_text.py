# Hotel Management System : nouveau texte fourni par le titulaire.

from django.db import migrations

SLUG = 'hotel-management-system'

NEW_DESCRIPTION = (
    "Une plateforme de gestion hôtelière qui regroupe les réservations, les paiements, "
    "les arrivées, les départs et les réclamations au même endroit. Les informations sont "
    "mises à jour en temps réel pour limiter les erreurs, éviter les incohérences et "
    "faciliter la gestion quotidienne des séjours."
)

OLD_DESCRIPTION = (
    "Une plateforme de gestion hôtelière qui centralise réservations, paiements, arrivées, "
    "départs et réclamations pour éviter les erreurs et les conflits de données. Les "
    "informations sont synchronisées instantanément, garantissant une gestion fluide et "
    "fiable des séjours."
)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_hotel_management_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
