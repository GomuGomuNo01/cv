from django.db import migrations

# (project_slug, [(order, image_path), ...]) — l'image déjà en place (index 0)
# n'est pas répétée ici, seules les images supplémentaires de la galerie.
GALLERY_IMAGES = {
    'maven-toys-powerbi': [
        (1, 'projects/gallery/maven-toys-02.png'),
        (2, 'projects/gallery/maven-toys-03.png'),
        (3, 'projects/gallery/maven-toys-04.png'),
    ],
    'contoso-sales-powerbi': [
        (1, 'projects/gallery/contoso-02.png'),
        (2, 'projects/gallery/contoso-03.png'),
        (3, 'projects/gallery/contoso-04.png'),
    ],
    'sbs-bank': [
        (1, 'projects/gallery/sbs-bank-02.png'),
        (2, 'projects/gallery/sbs-bank-03.png'),
        (3, 'projects/gallery/sbs-bank-04.png'),
    ],
    'automatisation-de-processus': [
        (1, 'projects/gallery/automatisation-02.png'),
    ],
    'sales-report-automation': [
        (1, 'projects/gallery/sales-report-02.png'),
        (2, 'projects/gallery/sales-report-03.png'),
        (3, 'projects/gallery/sales-report-04.png'),
    ],
    'hospital': [
        (1, 'projects/gallery/hospital-02.png'),
        (2, 'projects/gallery/hospital-03.png'),
        (3, 'projects/gallery/hospital-04.png'),
        (4, 'projects/gallery/hospital-05.png'),
    ],
}

# Missions détaillées par entreprise, une ligne par tâche réellement
# effectuée (mêmes faits déjà utilisés sur les CV cette session).
COMPANY_TASKS = {
    'madameb0nplan': """Recueilli les besoins des équipes métier en atelier pour cadrer les indicateurs de suivi
Automatisé la collecte de données via des scripts Python
Fiabilisé des bases de données SQL via nettoyage et contrôles qualité
Piloté l'alimentation de tableaux de bord Power BI restitués quotidiennement à l'équipe""",
    'IT-CENTREX': """Conçu des modèles de détection d'anomalies (scikit-learn) sur des données de production
Développé des API REST (Java, Python) connectant plusieurs systèmes existants
Fiabilisé des traitements de données répétitifs, réduisant le travail manuel des équipes
Testé et documenté les résultats de tests fonctionnels avant chaque mise en production""",
    'TASNIM SOLUTION': """Développé des applications web avec Laravel (MVC, ORM Eloquent, Blade)
Développé une application C# d'automatisation""",
    'Institut Pasteur de Côte d’Ivoire': """Conçu et administré des bases de données relationnelles (MySQL, SQL Server) via modélisation et migration
Développé une application interne testée et utilisée par du personnel non technique, avec gestion des accès par rôle""",
}


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    Company = apps.get_model('core', 'Company')

    for slug, images in GALLERY_IMAGES.items():
        try:
            project = Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            continue
        for order, path in images:
            ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})

    for name, tasks in COMPANY_TASKS.items():
        Company.objects.filter(name=name).update(description=tasks)


def unpopulate(apps, schema_editor):
    ProjectImage = apps.get_model('core', 'ProjectImage')
    ProjectImage.objects.filter(project__slug__in=GALLERY_IMAGES.keys()).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_project_image_gallery'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
