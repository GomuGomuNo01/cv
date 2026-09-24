# Ajoute les captures d'écran réelles de la documentation Swagger de
# l'API REST JWT (fournies par l'utilisateur, ce dépôt n'ayant aucune
# image dans son dépôt GitHub).

from django.db import migrations

PRIMARY_IMAGE = 'projects/api-rest-jwt.webp'
GALLERY_IMAGES = [
    (1, 'projects/gallery/api-rest-jwt-02.webp'),
]


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    try:
        project = Project.objects.get(slug='api-rest-jwt')
    except Project.DoesNotExist:
        return

    project.image = PRIMARY_IMAGE
    project.save()

    for order, path in GALLERY_IMAGES:
        ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    try:
        project = Project.objects.get(slug='api-rest-jwt')
    except Project.DoesNotExist:
        return
    project.image = None
    project.save()
    ProjectImage.objects.filter(project=project).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_webp_optimized_images'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
