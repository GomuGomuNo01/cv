# SBS Bank : nouveau texte fourni par le titulaire, et même présentation que
# les autres projets vidéo (titre, lien "Présentation" et image ouvrent la
# vidéo de 40 s en plein écran ; l'affiche remplace le GIF et la galerie).
# Bouton .pbix conservé. Vidéo et affiche reprises du dépôt
# Simple-Banking-System-Python (assets/video/). Position inchangée : 07,
# juste après NYC Taxi.

from django.db import migrations

SLUG = 'sbs-bank'
VIDEO = 'core/videos/sbs-bank-presentation.mp4'
POSTER = 'projects/sbs-bank-poster.webp'

NEW_DESCRIPTION = (
    "Une banque en ligne souhaite vérifier si ses partenaires lui apportent des clients "
    "actifs. L’analyse de 254 000 opérations sur 18 mois révèle que ces clients utilisent "
    "leur compte deux fois moins souvent que les autres. Ces résultats permettent de "
    "proposer six actions prioritaires pour améliorer leur activité."
)

OLD_DESCRIPTION = (
    "Une néobanque simulée veut vérifier si ses partenaires commerciaux lui apportent "
    "des clients réellement actifs. L'analyse de 254 000 opérations sur 18 mois montre "
    "que les clients issus de ces partenaires utilisent leur compte deux fois moins "
    "souvent que les autres, ce qui permet de formuler six recommandations commerciales "
    "prioritaires."
)
OLD_IMAGE = 'projects/sbs-bank-demo.gif'
OLD_GALLERY = [
    (0, 'projects/sbs-bank.webp'),
    (2, 'projects/gallery/sbs-bank-02.webp'),
    (3, 'projects/gallery/sbs-bank-03.webp'),
    (4, 'projects/gallery/sbs-bank-04.webp'),
]


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
        ('core', '0056_nyc_taxi_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
