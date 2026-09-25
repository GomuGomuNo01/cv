# Ajoute le projet Système de Gestion Hôtelière (La baie des lacs),
# rendu public sur GitHub. Aucune image dans le dépôt (juste un favicon) :
# illustration générique en SVG, comme pour les autres projets sans capture.

from django.db import migrations

PROJECT = dict(
    index_number='12', title='Système de Gestion Hôtelière', slug='hotel-management-system',
    short_description=(
        "Application complète de réservation et gestion d'hôtel : catalogue de chambres, "
        "réservations sans conflit de dates, paiements en ligne, suivi en temps réel des "
        "arrivées et départs. Validée par 259 tests automatisés (174 backend, 85 frontend)."
    ),
    tech_stack='Laravel,React,MySQL,WebSocket',
    github_link='https://github.com/GomuGomuNo01/hotel-management-system',
    live_link='',
    image='projects/hotel-management-generic.svg',
    is_featured=True,
    in_progress=False,
)


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.get_or_create(slug=PROJECT['slug'], defaults=PROJECT)


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=PROJECT['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_generic_illustrations'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
