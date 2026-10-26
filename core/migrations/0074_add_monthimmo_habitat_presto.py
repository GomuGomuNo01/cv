# Ajoute le projet « Suivi des demandes Habitat Presto » (cas pratique Month'immo),
# catégorie Data & IA. Source : dépôt GomuGomuNo01/monthimmo-cas-pratique.
# Les captures proviennent du dépôt et ne montrent que des données fictives.
#
# Le nouveau projet prend le numéro 09 de la catégorie Data & IA : les projets
# Développement sont décalés d'un cran pour éviter deux projets numérotés 09.

from django.db import migrations

NEW_PROJECT = dict(
    title='Suivi des demandes Habitat Presto',
    slug='monthimmo-habitat-presto',
    category='data',
    index_number='09',
    short_description=(
        "Le pôle travaux d'une entreprise reçoit des demandes clients par email, qu'il faut "
        "recopier à la main sous peine de les oublier. Un workflow n8n lit chaque demande avec "
        "Claude Haiku, la range dans un tableau Airtable sans doublon et alerte le conducteur "
        "de travaux par Gmail. Il gère les demandes incomplètes et les pannes du service de "
        "lecture. Plus de vingt scénarios sont testés, sur des données fictives."
    ),
    tech_stack='n8n,Claude Haiku,Airtable,Gmail',
    github_link='https://github.com/GomuGomuNo01/monthimmo-cas-pratique',
    image='projects/monthimmo-habitat-presto.webp',
    is_featured=True,
    in_progress=False,
)

GALLERY = [(i, f'projects/gallery/monthimmo-habitat-presto-0{i}.webp') for i in range(2, 7)]

# slug : (nouveau numéro, ancien numéro)
RENUMBER = {
    'hotel-management-system': ('10', '09'),
    'site-amid-2026': ('11', '10'),
    'api-rest-jwt': ('12', '11'),
    'mini-crm-dotnet': ('13', '12'),
    'hospital': ('14', '13'),
}


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    ProjectImage = apps.get_model('core', 'ProjectImage')
    for slug, (new, old) in RENUMBER.items():
        Project.objects.filter(slug=slug, index_number=old).update(index_number=new)
    project, _ = Project.objects.get_or_create(slug=NEW_PROJECT['slug'], defaults=NEW_PROJECT)
    for order, path in GALLERY:
        ProjectImage.objects.get_or_create(project=project, order=order, defaults={'image': path})


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=NEW_PROJECT['slug']).delete()
    for slug, (new, old) in RENUMBER.items():
        Project.objects.filter(slug=slug, index_number=new).update(index_number=old)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_skills_n8n_airtable'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
