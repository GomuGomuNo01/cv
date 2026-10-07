# Retire Career-Ops du portfolio (demande du titulaire) et renumérote la
# section Développement pour supprimer le trou laissé en position 09.

from django.db import migrations

SLUG = 'career-ops'

CAREER_OPS = dict(
    title='Career-Ops',
    slug=SLUG,
    category='data',
    index_number='09',
    short_description=(
        "Postuler à plusieurs offres devient vite difficile à suivre quand les informations "
        "sont dispersées entre les annonces, les CV et les tableaux de suivi. Career-Ops est "
        "un framework open source d'agents IA que j'utilise pour centraliser mes "
        "candidatures, évaluer les offres et suivre leur statut automatiquement."
    ),
    tech_stack='Node.js,Go,Playwright,Agents IA',
    github_link='https://github.com/GomuGomuNo01/career-ops',
    live_link='',
    image='projects/maintenance-generic.svg',
    is_featured=True,
    in_progress=True,
)

NEW_ORDER = [
    ('hotel-management-system', '09'),
    ('api-rest-jwt', '10'),
    ('mini-crm-dotnet', '11'),
    ('hospital', '12'),
    ('instagram-unlike-cleaner', '13'),
]

OLD_ORDER = [
    ('hotel-management-system', '10'),
    ('api-rest-jwt', '11'),
    ('mini-crm-dotnet', '12'),
    ('hospital', '13'),
    ('instagram-unlike-cleaner', '14'),
]


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).delete()
    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.get_or_create(slug=SLUG, defaults=CAREER_OPS)
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_docassist_presentation_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
