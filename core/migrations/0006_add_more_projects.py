# Ajoute 5 nouveaux projets réels (Contoso, Telco Churn, Sales Report
# Automation, API REST JWT, Hospital) et renumérote l'ensemble pour garder
# la hiérarchie Data > IA/Automatisation > Développement.

from django.db import migrations

# (slug, nouveau index_number) pour les projets déjà en base
REINDEX = [
    ('sbs-bank', '05'),
    ('automatisation-de-processus', '07'),
    ('mini-crm-dotnet', '09'),
]

NEW_PROJECTS = [
    dict(
        index_number='04', title='Contoso Sales Analytics (Power BI)', slug='contoso-sales-powerbi',
        short_description=(
            "Révèle une baisse de chiffre d'affaires de 33 % (43,8M$ → 29,3M$) et identifie "
            "les catégories de produits les plus touchées. Analyse de 225 000 ventes."
        ),
        tech_stack='Power BI,DAX',
        github_link='https://github.com/GomuGomuNo01/contoso-sales-powerbi',
        live_link='',
    ),
    dict(
        index_number='06', title='Telco Churn Prediction', slug='telco-churn-prediction',
        short_description=(
            "Compare 9 modèles de machine learning sur 7 043 clients télécoms pour anticiper "
            "la résiliation, et détecte près d'un tiers de clients à risque en plus grâce au "
            "modèle retenu. Déployé dans une application Streamlit temps réel."
        ),
        tech_stack='Python,scikit-learn,Streamlit',
        github_link='https://github.com/GomuGomuNo01/telco-churn-prediction',
        live_link='',
    ),
    dict(
        index_number='08', title='Sales Report Automation', slug='sales-report-automation',
        short_description=(
            "Génère automatiquement un rapport de ventes en 7 secondes, contre 5 heures à la "
            "main. Rapport PDF de 6 pages, validé par plus de 50 tests automatisés."
        ),
        tech_stack='Python,Automatisation,PDF',
        github_link='https://github.com/GomuGomuNo01/sales-report-automation',
        live_link='',
    ),
    dict(
        index_number='10', title='API REST JWT', slug='api-rest-jwt',
        short_description=(
            "Gère la création de comptes, la connexion sécurisée et les droits d'accès d'une "
            "application, avec réinitialisation de mot de passe par email. Déployé en "
            "production, documenté via Swagger."
        ),
        tech_stack='Java,Spring Boot,JWT,MySQL',
        github_link='https://github.com/GomuGomuNo01/api-rest-jwt',
        live_link='https://jwt-api-gkdg.onrender.com/swagger-ui.html',
    ),
    dict(
        index_number='11', title='Hospital', slug='hospital',
        short_description=(
            "Permet à une équipe médicale de gérer des dossiers patients avec traçabilité "
            "complète des actions et double authentification pour les comptes sensibles. "
            "Trois profils d'accès distincts (administrateur, médecin, infirmier)."
        ),
        tech_stack='PHP,Laravel,MySQL',
        github_link='https://github.com/GomuGomuNo01/Hospital',
        live_link='',
    ),
]


def populate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')

    for slug, new_index in REINDEX:
        Project.objects.filter(slug=slug).update(index_number=new_index)

    for data in NEW_PROJECTS:
        Project.objects.get_or_create(slug=data['slug'], defaults=data)


def unpopulate(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=[p['slug'] for p in NEW_PROJECTS]).delete()
    Project.objects.filter(slug='sbs-bank').update(index_number='04')
    Project.objects.filter(slug='automatisation-de-processus').update(index_number='05')
    Project.objects.filter(slug='mini-crm-dotnet').update(index_number='06')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_populate_education'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
