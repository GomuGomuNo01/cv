# Retire les projets Hospital et Telco Churn Prediction du portfolio,
# retire le lien "Code" du projet Hotel Management System (seule la
# "Présentation" reste affichée) et renumérote les projets restants pour
# ne laisser aucun trou dans la numérotation.

from django.db import migrations

REMOVED_SLUGS = ['hospital', 'telco-churn-prediction']
HOTEL_SLUG = 'hotel-management-system'


def _sort_key(project):
    try:
        return (int(project.index_number), project.pk)
    except (TypeError, ValueError):
        return (10_000, project.pk)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=REMOVED_SLUGS).delete()
    Project.objects.filter(slug=HOTEL_SLUG).update(github_link='')
    for position, project in enumerate(sorted(Project.objects.all(), key=_sort_key), start=1):
        new_index = f'{position:02d}'
        if project.index_number != new_index:
            Project.objects.filter(pk=project.pk).update(index_number=new_index)


def revert_old(apps, schema_editor):
    # Suppression de données : non restaurable automatiquement.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_contoso_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
