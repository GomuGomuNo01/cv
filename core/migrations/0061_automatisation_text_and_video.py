# Automatisation de processus : nouveau texte fourni par le titulaire, et
# même présentation que DocAssist, IUC et les autres projets vidéo (titre,
# lien "Présentation" et image ouvrent la vidéo de 40 s en plein écran ;
# l'affiche remplace l'image et la galerie). Lien Démo (Codespaces) et lien
# Code conservés. Vidéo et affiche reprises du dépôt
# automatisation-de-processus (assets/video/).

from django.db import migrations

SLUG = 'automatisation-de-processus'
VIDEO = 'core/videos/automatisation-de-processus-presentation.mp4'
POSTER = 'projects/automatisation-de-processus-poster.webp'

NEW_DESCRIPTION = (
    "Six tâches répétitives, comme le suivi des stocks, l’envoi d’e-mails et la collecte "
    "de données en ligne, sont automatisées grâce à des scripts Python. Testés avant chaque "
    "mise en service, ces outils fonctionnent de manière fiable depuis deux ans et "
    "permettent de gagner du temps au quotidien."
)

OLD_DESCRIPTION = (
    "Six tâches manuelles (suivi de stock, envoi d'e-mails et collecte de données en ligne) "
    "mobilisent du temps chaque semaine. Ces scripts Python exécutent désormais les "
    "opérations seuls, sont testés avant chaque mise en production et fonctionnent en "
    "service depuis deux ans."
)
OLD_IMAGE = 'projects/automatisation-de-processus.webp'
OLD_GALLERY = [(1, 'projects/gallery/automatisation-02.webp')]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION, video_url=VIDEO, image=POSTER)
    ProjectImage.objects.filter(project__slug=SLUG).delete()


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION, video_url='', image=OLD_IMAGE)
    project = Project.objects.filter(slug=SLUG).first()
    if project:
        for order, path in OLD_GALLERY:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_iuc_github_link'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
