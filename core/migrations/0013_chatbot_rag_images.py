# Ajoute les captures d'écran réelles de la démo Chatbot RAG - DocAssist
# (fournies directement par l'utilisateur, ce projet n'ayant aucune image
# dans son dépôt GitHub).

from django.db import migrations

PRIMARY_IMAGE = 'projects/chatbot-rag.webp'
GALLERY_IMAGES = [
    (1, 'projects/gallery/chatbot-rag-02.webp'),
    (2, 'projects/gallery/chatbot-rag-03.webp'),
]


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    try:
        project = Project.objects.get(slug='chatbot-rag-docassist')
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
        project = Project.objects.get(slug='chatbot-rag-docassist')
    except Project.DoesNotExist:
        return
    project.image = None
    project.save()
    ProjectImage.objects.filter(project=project).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_gif_previews'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
