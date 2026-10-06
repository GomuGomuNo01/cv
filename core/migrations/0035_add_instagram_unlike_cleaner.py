# Ajoute le projet Instagram Unlike Cleaner (IUC) : projet personnel,
# entièrement développé par le titulaire (32 commits, aucun fork).
#
# À la demande explicite du titulaire, le lien vers le dépôt GitHub n'est
# pas affiché (pas de bouton "Code"). La démo en ligne (données fictives,
# sans compte requis) est affichée à la place.

from django.db import migrations

NEW_PROJECT = dict(
    title='Instagram Unlike Cleaner',
    slug='instagram-unlike-cleaner',
    category='dev',
    index_number='14',
    short_description=(
        "Une personne veut effacer des années de likes Instagram sans confier son mot de "
        "passe ni ses données. IUC, outil 100 % local, cible les likes avec le filtre "
        "d'Instagram, les liste pour validation puis les retire par lots prudents : 1 493 "
        "likes recensés en 14 min sur un vrai compte, et 283 tests prouvent qu'aucun "
        "identifiant n'est lu ni conservé."
    ),
    tech_stack='Python,Playwright,FastAPI,React,TypeScript',
    github_link='',
    live_link='https://gomugomuno01.github.io/Instagram-Unlike-Cleaner/',
    image='projects/instagram-unlike-cleaner-demo.gif',
    is_featured=True,
    in_progress=False,
)

GALLERY = [
    (1, 'projects/gallery/instagram-unlike-cleaner-01.webp'),
    (2, 'projects/gallery/instagram-unlike-cleaner-02.webp'),
    (3, 'projects/gallery/instagram-unlike-cleaner-03.webp'),
    (4, 'projects/gallery/instagram-unlike-cleaner-04.webp'),
    (5, 'projects/gallery/instagram-unlike-cleaner-05.webp'),
    (6, 'projects/gallery/instagram-unlike-cleaner-06.webp'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')

    project, _ = Project.objects.get_or_create(slug=NEW_PROJECT['slug'], defaults=NEW_PROJECT)
    for order, path in GALLERY:
        ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=NEW_PROJECT['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_career_ops_in_progress'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
