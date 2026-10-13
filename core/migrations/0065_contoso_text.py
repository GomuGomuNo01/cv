# Contoso Sales Analytics : nouveau texte fourni par le titulaire.

from django.db import migrations

SLUG = 'contoso-sales-powerbi'

NEW_DESCRIPTION = (
    "Le chiffre d’affaires d’une entreprise baisse de 33 %, passant de 43,8 M$ à 29,3 M$. "
    "L’analyse de 225 000 ventes permet d’identifier les produits et les clients les plus "
    "touchés. Un tableau de bord Power BI présente les résultats pour aider la direction "
    "commerciale à comprendre cette baisse et à prendre des décisions adaptées."
)

OLD_DESCRIPTION = (
    "Le chiffre d’affaires d’une entreprise baisse de 33 %, passant de 43,8 M$ à 29,3 M$, "
    "sans raison clairement identifiée. L’analyse de 225 000 ventes permet d’identifier les "
    "produits et les types de clients les plus concernés par cette baisse. Les résultats sont "
    "ensuite présentés dans un tableau de bord Power BI pour aider la direction commerciale à "
    "comprendre la situation et à prendre les bonnes décisions."
)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_tech_from_repos'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
