# Chatbot RAG · DocAssist : vidéo de présentation (40 s) ouverte en plein
# écran depuis le titre, le lien "Présentation" et l'image de la carte.
# L'image de la carte devient l'affiche de la vidéo, à la place de la
# capture et de la galerie.
#
# Vidéo reprise du dépôt Chatbot-RAG (branche docs/readme-portfolio-video,
# assets/video/DocAssist_presentation.mp4) et ré-encodée (H.264, CRF 26,
# yuv420p, faststart) : 17 Mo -> 5,2 Mo, sans perte visible. Servie comme
# fichier statique par WhiteNoise (requêtes partielles pour Safari / iOS).

from django.db import migrations

SLUG = 'chatbot-rag-docassist'
VIDEO = 'core/videos/chatbot-rag-docassist-presentation.mp4'
POSTER = 'projects/chatbot-rag-docassist-poster.webp'

OLD_IMAGE = 'projects/chatbot-rag.webp'
OLD_GALLERY = [
    (1, 'projects/gallery/chatbot-rag-02.webp'),
    (2, 'projects/gallery/chatbot-rag-03.webp'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url=VIDEO, image=POSTER)
    ProjectImage.objects.filter(project__slug=SLUG).delete()


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(video_url='', image=OLD_IMAGE)
    project = Project.objects.filter(slug=SLUG).first()
    if project:
        for order, path in OLD_GALLERY:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_iuc_video_self_hosted'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
