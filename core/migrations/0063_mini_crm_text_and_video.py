# Mini-CRM : nouveau texte fourni par le titulaire, et même présentation que
# DocAssist, IUC et les autres projets vidéo (titre, lien "Présentation" et
# image ouvrent la vidéo de 60 s en plein écran ; l'affiche remplace
# l'illustration générique). Vidéo et affiche reprises du dépôt mini_crm
# (assets/video/).

from django.db import migrations

SLUG = 'mini-crm-dotnet'
VIDEO = 'core/videos/mini-crm-presentation.mp4'
POSTER = 'projects/mini-crm-poster.webp'
OLD_IMAGE = 'projects/mini-crm-generic.svg'

NEW_DESCRIPTION = (
    "Les informations sur les clients et les contrats sont souvent dispersées entre "
    "plusieurs fichiers et e-mails. Cette application les regroupe au même endroit, "
    "présente les indicateurs clés dans un tableau de bord et organise les données pour "
    "faciliter le suivi des clients et la gestion commerciale."
)

OLD_DESCRIPTION = (
    "Les informations clients et contrats sont souvent dispersées entre des tableurs et des "
    "e-mails. Cette application centralise leur suivi, restitue les indicateurs clés dans un "
    "tableau de bord et conserve les données dans une base structurée pour faciliter le "
    "pilotage commercial."
)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION, video_url=VIDEO, image=POSTER)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION, video_url='', image=OLD_IMAGE)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_automatisation_demo_streamlit'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
