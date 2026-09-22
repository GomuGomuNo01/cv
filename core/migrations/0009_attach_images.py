# Corrige un bug de reproductibilité : les images de projets et les logos
# de formation avaient été attachés à la main via `manage.py shell` sur la
# base locale (non versionnée), jamais via une migration. Sur un clone
# neuf (fresh clone + migrate), aucune image ne s'affichait alors même
# que les fichiers existent bien dans media/. Cette migration répare ça
# en fixant les champs image/logo à partir des fichiers déjà présents
# dans le repo.

from django.db import migrations

PROJECT_IMAGES = {
    'maven-toys-powerbi': 'projects/maven-toys-powerbi.png',
    'sbs-bank': 'projects/sbs-bank.png',
    'automatisation-de-processus': 'projects/automatisation-de-processus.png',
    'contoso-sales-powerbi': 'projects/contoso-sales-powerbi.png',
    'hospital': 'projects/hospital.png',
    'sales-report-automation': 'projects/sales-report-automation.png',
}

EDUCATION_LOGOS = {
    'ESGI Paris': 'education/ESGI.png',
    'ESIIA Torcy': 'education/ESIIA.png',
    'PIGIER Côte d’Ivoire': 'education/PIGIER.jpg',
}


def attach(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Education = apps.get_model('core', 'Education')

    for slug, path in PROJECT_IMAGES.items():
        Project.objects.filter(slug=slug).update(image=path)

    for school, path in EDUCATION_LOGOS.items():
        Education.objects.filter(school=school).update(logo=path)


def detach(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Education = apps.get_model('core', 'Education')

    Project.objects.filter(slug__in=PROJECT_IMAGES.keys()).update(image=None)
    Education.objects.filter(school__in=EDUCATION_LOGOS.keys()).update(logo=None)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_project_in_progress'),
    ]

    operations = [
        migrations.RunPython(attach, detach),
    ]
