# Bascule les images statiques de projets (PNG) vers des versions WebP
# redimensionnées et compressées (~60 % plus légères), pour accélérer le
# chargement de la page. Les fichiers .png correspondants ont été
# supprimés du dépôt et remplacés par les .webp.

from django.db import migrations


def to_webp(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    for p in Project.objects.filter(image__iendswith='.png'):
        p.image = p.image.name[:-4] + '.webp'
        p.save()

    for gi in ProjectImage.objects.filter(image__iendswith='.png'):
        gi.image = gi.image.name[:-4] + '.webp'
        gi.save()


def to_png(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    for p in Project.objects.filter(image__iendswith='.webp'):
        p.image = p.image.name[:-5] + '.png'
        p.save()

    for gi in ProjectImage.objects.filter(image__iendswith='.webp'):
        gi.image = gi.image.name[:-5] + '.png'
        gi.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_chatbot_rag_images'),
    ]

    operations = [
        migrations.RunPython(to_webp, to_png),
    ]
