# Ajoute le projet Site AMID 2026 (African Mobility & Innovation Day, 20 ans),
# conçu et développé avec Charles Sorgho pour le Pôle IT & Data Management de
# l'African Business Club. Description et pile technique relevées dans le dépôt
# abclumni (frontend/amid), aligné sur la fiche projet LinkedIn. Le dépôt est
# privé (organisation African-Business-Club) : pas de lien "Code", seulement la
# démo en ligne. L'affiche reprend la page d'accueil du site.
#
# Passe en dernier de la catégorie Développement (12).

from django.db import migrations

PROJECT = dict(
    index_number='12', title='Site AMID 2026', slug='site-amid-2026',
    category='dev',
    short_description=(
        "Les 20 ans de l'African Mobility & Innovation Day (24 octobre 2026, ESCP Paris 17e) "
        "avaient besoin d'un site où les participants trouvent le programme, les intervenants, "
        "les partenaires et l'accès au campus, en français et en anglais. Conçu et développé "
        "avec Charles Sorgho pour le Pôle IT & Data Management de l'African Business Club : "
        "React 19 et TypeScript strict, carte du campus, contrôle automatique des traductions "
        "avant chaque build, déploiement avec Docker et GitHub Actions. Les informations non "
        "confirmées (salles, certains horaires) s'affichent « à confirmer » plutôt que d'être "
        "inventées."
    ),
    tech_stack='React,TypeScript,Vite,React Router,Leaflet,Docker,GitHub Actions',
    github_link='',
    live_link='https://reseau.africanbusinessclub.org/amid/',
    image='projects/site-amid-2026-poster.webp',
    is_featured=True,
    in_progress=False,
)


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.get_or_create(slug=PROJECT['slug'], defaults=PROJECT)


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=PROJECT['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_linkedin_experience_octobre'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
