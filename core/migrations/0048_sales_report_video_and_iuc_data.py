# 1. Sales Report Automation reprend la présentation de DocAssist et d'IUC :
#    vidéo de présentation (40 s) ouverte en plein écran depuis le titre, le
#    lien "Présentation" et l'image de la carte ; l'image devient l'affiche
#    de la vidéo, à la place de la capture et de la galerie.
#    Vidéo et affiche reprises du dépôt sales-report-automation
#    (assets/video/), vidéo servie comme fichier statique par WhiteNoise.
# 2. Instagram Unlike Cleaner passe de "Développement" à "Data & IA", placé à
#    la fin de la section (09) ; la section Développement est renumérotée.

from django.db import migrations

SALES = 'sales-report-automation'
SALES_VIDEO = 'core/videos/sales-report-automation-presentation.mp4'
SALES_POSTER = 'projects/sales-report-automation-poster.webp'
SALES_OLD_IMAGE = 'projects/sales-report-automation.webp'
SALES_OLD_GALLERY = [
    (1, 'projects/gallery/sales-report-02.webp'),
    (2, 'projects/gallery/sales-report-03.webp'),
    (3, 'projects/gallery/sales-report-04.webp'),
]

IUC = 'instagram-unlike-cleaner'

NEW_ORDER = [
    (IUC, 'data', '09'),
    ('hotel-management-system', 'dev', '10'),
    ('api-rest-jwt', 'dev', '11'),
    ('mini-crm-dotnet', 'dev', '12'),
    ('hospital', 'dev', '13'),
]

OLD_ORDER = [
    ('hotel-management-system', 'dev', '09'),
    ('api-rest-jwt', 'dev', '10'),
    ('mini-crm-dotnet', 'dev', '11'),
    ('hospital', 'dev', '12'),
    (IUC, 'dev', '13'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    Project.objects.filter(slug=SALES).update(video_url=SALES_VIDEO, image=SALES_POSTER)
    ProjectImage.objects.filter(project__slug=SALES).delete()

    for slug, category, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(category=category, index_number=index)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    Project.objects.filter(slug=SALES).update(video_url='', image=SALES_OLD_IMAGE)
    project = Project.objects.filter(slug=SALES).first()
    if project:
        for order, path in SALES_OLD_GALLERY:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})

    for slug, category, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(category=category, index_number=index)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_sales_report_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
