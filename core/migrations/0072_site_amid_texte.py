# Site AMID 2026 : nouveau texte fourni par le titulaire pour la carte du
# portfolio (objectif du site, public visé, qualité de l'information), à la
# place de la description technique initiale.

from django.db import migrations

SLUG = 'site-amid-2026'

NEW_DESCRIPTION = (
    "Créer un site web bilingue (français et anglais) pour les 20 ans de l’African "
    "Mobility & Innovation Day, afin de permettre aux participants de retrouver "
    "facilement le programme, les intervenants, les partenaires et les informations "
    "pratiques pour accéder au campus de l’ESCP Paris. Le site offre une expérience "
    "simple et claire, tout en garantissant des informations fiables."
)

OLD_DESCRIPTION = (
    "Les 20 ans de l'African Mobility & Innovation Day (24 octobre 2026, ESCP Paris 17e) "
    "avaient besoin d'un site où les participants trouvent le programme, les intervenants, "
    "les partenaires et l'accès au campus, en français et en anglais. Conçu et développé "
    "avec Charles Sorgho pour le Pôle IT & Data Management de l'African Business Club : "
    "React 19 et TypeScript strict, carte du campus, contrôle automatique des traductions "
    "avant chaque build, déploiement avec Docker et GitHub Actions. Les informations non "
    "confirmées (salles, certains horaires) s'affichent « à confirmer » plutôt que d'être "
    "inventées."
)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_amid_consulter_et_ordre'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
