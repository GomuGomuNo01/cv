# Contoso Sales Analytics et Maven Toys Analytics : nouveaux textes fournis
# par le titulaire.

from django.db import migrations

NEW = {
    'contoso-sales-powerbi': (
        "Le chiffre d’affaires d’une entreprise baisse de 33 %, passant de 43,8 M$ à "
        "29,3 M$, sans raison clairement identifiée. L’analyse de 225 000 ventes permet "
        "d’identifier les produits et les types de clients les plus concernés par cette "
        "baisse. Les résultats sont ensuite présentés dans un tableau de bord Power BI pour "
        "aider la direction commerciale à comprendre la situation et à prendre les bonnes "
        "décisions."
    ),
    'maven-toys-powerbi': (
        "Analyse de plus de 829 000 ventes d’une chaîne de 50 magasins pour identifier les "
        "causes de baisse de rentabilité. Mise en évidence de 29 069 $ de pertes mensuelles "
        "liées aux ruptures de stock et création d’un outil Power BI pour faciliter la "
        "prise de décision."
    ),
}

OLD = {
    'contoso-sales-powerbi': (
        "Le chiffre d'affaires d'un distributeur recule de 33 % (43,8 M$ à 29,3 M$), sans "
        "explication claire. L'analyse de 225 000 ventes identifie les catégories et "
        "segments les plus touchés, puis restitue le diagnostic à la direction commerciale "
        "dans un dashboard Power BI conçu pour faciliter la prise de décision."
    ),
    'maven-toys-powerbi': (
        "Une enseigne de 50 magasins voit son chiffre d'affaires progresser, mais sa marge "
        "se dégrade. L'analyse de 829 262 ventes révèle que les ruptures de stock "
        "représentent un manque à gagner estimé à 29 069 $ par mois, puis transforme ce "
        "constat en recommandations concrètes grâce à un dashboard Power BI."
    ),
}


def set_texts(texts):
    def run(apps, schema_editor):
        Project = apps.get_model('core', 'Project')
        for slug, text in texts.items():
            Project.objects.filter(slug=slug).update(short_description=text)
    return run


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_contoso_video_and_order'),
    ]

    operations = [
        migrations.RunPython(set_texts(NEW), set_texts(OLD)),
    ]
