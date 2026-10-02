# Ajoute Career-Ops au portfolio, à la demande explicite du titulaire.
#
# Important : github.com/GomuGomuNo01/career-ops est un FORK de
# career-ops-hq/career-ops (383 commits de son auteur d'origine, aucun
# commit du titulaire). La description reste donc factuelle : un outil
# open source qu'il UTILISE pour sa recherche d'alternance, jamais
# présenté comme développé par lui. Aucune image n'est définie (le
# visuel du dépôt d'origine ne lui appartient pas) ; la carte retombe
# sur l'illustration générique par défaut.

from django.db import migrations

NEW_ORDER = [
    ('nyc-taxi-data-engineering', '01'),
    ('maven-toys-powerbi', '02'),
    ('contoso-sales-powerbi', '03'),
    ('sbs-bank', '04'),
    ('telco-churn-prediction', '05'),
    ('chatbot-rag-docassist', '06'),
    ('sales-report-automation', '07'),
    ('automatisation-de-processus', '08'),
    ('career-ops', '09'),
    ('hotel-management-system', '10'),
    ('api-rest-jwt', '11'),
    ('mini-crm-dotnet', '12'),
    ('hospital', '13'),
]

OLD_ORDER = [
    ('hotel-management-system', '09'),
    ('api-rest-jwt', '10'),
    ('mini-crm-dotnet', '11'),
    ('hospital', '12'),
]

CAREER_OPS = dict(
    title='Career-Ops',
    slug='career-ops',
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
    is_featured=True,
    in_progress=False,
)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.get_or_create(slug=CAREER_OPS['slug'], defaults=CAREER_OPS)
    for slug, index in NEW_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=CAREER_OPS['slug']).delete()
    for slug, index in OLD_ORDER:
        Project.objects.filter(slug=slug).update(index_number=index)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_sales_report_demo_link'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
