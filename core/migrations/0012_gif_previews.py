# Remplace l'image de référence (aperçu principal) de 3 projets par un
# GIF animé issu de leur dépôt GitHub, quand il en existe un. L'ancienne
# image statique utilisée comme aperçu rejoint la galerie plutôt que
# d'être perdue.

from django.db import migrations
from django.db.models import F

GIF_PREVIEWS = {
    # slug: (chemin du gif, chemin de l'ancienne image statique à conserver dans la galerie)
    'maven-toys-powerbi': ('projects/maven-toys-demo.gif', 'projects/maven-toys-powerbi.png'),
    'contoso-sales-powerbi': ('projects/contoso-demo.gif', 'projects/contoso-sales-powerbi.png'),
    'sbs-bank': ('projects/sbs-bank-demo.gif', 'projects/sbs-bank.png'),
}


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    for slug, (gif_path, old_static_path) in GIF_PREVIEWS.items():
        try:
            project = Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            continue
        # L'ancienne image statique (déjà l'aperçu) rejoint la galerie en
        # première position, avant les captures déjà présentes.
        ProjectImage.objects.filter(project=project).update(order=F('order') + 1)
        ProjectImage.objects.get_or_create(project=project, order=0, defaults={'image': old_static_path})
        project.image = gif_path
        project.save()


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, (gif_path, old_static_path) in GIF_PREVIEWS.items():
        Project.objects.filter(slug=slug).update(image=old_static_path)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_populate_gallery_and_tasks'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
