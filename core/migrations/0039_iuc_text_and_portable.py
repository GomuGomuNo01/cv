# Instagram Unlike Cleaner : nouveau texte fourni par le titulaire, et
# ajout du lien de téléchargement de la version portable (.zip) à côté de
# l'installeur Windows.

from django.db import migrations

SLUG = 'instagram-unlike-cleaner'

NEW_DESCRIPTION = (
    "IUC permet de nettoyer ses anciens likes Instagram en toute sécurité, sans partager "
    "son mot de passe ni ses données. L’outil fonctionne 100 % en local : il identifie les "
    "likes grâce aux filtres Instagram, les soumet à validation, puis les supprime par lots "
    "contrôlés.\n"
    "Résultat : 1 493 likes analysés en 14 minutes sur un compte réel, avec 283 tests "
    "confirmant qu’aucun identifiant n’est lu ou conservé."
)

OLD_DESCRIPTION = (
    "Une personne veut effacer des années de likes Instagram sans confier son mot de "
    "passe ni ses données. IUC, outil 100 % local, cible les likes avec le filtre "
    "d'Instagram, les liste pour validation puis les retire par lots prudents : 1 493 "
    "likes recensés en 14 min sur un vrai compte, et 288 tests prouvent qu'aucun "
    "identifiant n'est lu ni conservé."
)

PORTABLE_LINK = 'https://github.com/GomuGomuNo01/Instagram-Unlike-Cleaner/releases/latest/download/IUC-portable.zip'
PORTABLE_LABEL = '.zip portable'


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(
        short_description=NEW_DESCRIPTION,
        download_link_alt=PORTABLE_LINK,
        download_label_alt=PORTABLE_LABEL,
    )


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(
        short_description=OLD_DESCRIPTION,
        download_link_alt='',
        download_label_alt='',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_project_download_alt'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
