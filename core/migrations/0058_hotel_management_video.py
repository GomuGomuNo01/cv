# Hotel Management System reprend la présentation de DocAssist et IUC :
# vidéo de présentation (60 s) ouverte en plein écran depuis le titre, le
# lien "Présentation" et l'image de la carte ; l'affiche de la vidéo
# remplace l'image de maintenance. Le badge "En cours" est conservé.
# Vidéo et affiche reprises du dépôt hotel-management-system
# (assets/video/), vidéo servie comme fichier statique par WhiteNoise.

from django.db import migrations

SLUG = 'hotel-management-system'
VIDEO = 'core/videos/hotel-management-presentation.mp4'
POSTER = 'projects/hotel-management-poster.webp'
OLD_IMAGE = 'projects/maintenance-generic.svg'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(video_url=VIDEO, image=POSTER)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(video_url='', image=OLD_IMAGE)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_sbs_bank_text_and_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
