# Réécrit les descriptions des projets pour qu'elles soient explicites,
# simples et compréhensibles par un lecteur non technicien (résultat
# et contexte d'abord, jargon technique réduit au minimum).

from django.db import migrations

DESCRIPTIONS = {
    'chatbot-rag-docassist': (
        "Assistant IA qui répond à des questions posées en langage naturel sur un ensemble "
        "de documents, en citant précisément la source de chaque réponse pour qu'elle reste "
        "vérifiable. Refuse de répondre plutôt que d'inventer une information absente des documents."
    ),
    'nyc-taxi-data-engineering': (
        "Nettoie et organise 500 000 trajets de taxis new-yorkais bruts et incomplets pour les "
        "rendre exploitables dans des analyses. Repère et documente chaque donnée invalide "
        "(2,3 % du total) au lieu de la supprimer en silence, pour que les résultats finaux "
        "restent fiables."
    ),
    'maven-toys-powerbi': (
        "Tableau de bord qui analyse les ventes de 50 magasins d'une enseigne de jouets "
        "(829 262 ventes) et révèle un problème caché : l'entreprise perd 29 069 $ par mois à "
        "cause de ruptures de stock, alors même que son chiffre d'affaires progresse."
    ),
    'contoso-sales-powerbi': (
        "Tableau de bord qui analyse 225 000 ventes pour comprendre une baisse de chiffre "
        "d'affaires de 33 % (de 43,8 à 29,3 millions de dollars), et identifie précisément "
        "quelles catégories de produits en sont responsables."
    ),
    'sbs-bank': (
        "Analyse le comportement de 1 800 clients d'une banque (254 000 opérations) et révèle "
        "que les clients recrutés via des partenaires activent leur compte deux fois moins "
        "souvent que les autres. Propose 6 recommandations concrètes pour corriger ce problème."
    ),
    'telco-churn-prediction': (
        "Prédit à l'avance quels clients d'un opérateur télécom risquent de résilier leur "
        "contrat, en comparant 9 méthodes de prédiction sur 7 043 clients. Le modèle retenu "
        "repère un tiers de clients à risque en plus que les méthodes classiques, pour agir "
        "avant leur départ. Accessible via une application en ligne."
    ),
    'automatisation-de-processus': (
        "Remplace 6 tâches répétitives qu'un employé ferait à la main : surveiller les stocks, "
        "envoyer une alerte par email en cas de rupture, relever les prix des concurrents. "
        "Fonctionne seul, sans intervention humaine, depuis 2 ans."
    ),
    'sales-report-automation': (
        "Crée automatiquement un rapport de ventes de 6 pages à partir des données de "
        "l'entreprise, en 7 secondes au lieu de 5 heures si une personne devait le faire à la "
        "main. Plus de 50 tests garantissent que le rapport reste exact à chaque génération."
    ),
    'mini-crm-dotnet': (
        "Application pour gérer des clients et leurs contrats : création, suivi, historique. "
        "Chaque utilisateur n'a accès qu'aux fonctions liées à son rôle (administrateur, "
        "commercial...), et 52 tests automatisés vérifient que l'application fonctionne "
        "correctement après chaque modification."
    ),
    'api-rest-jwt': (
        "Brique technique réutilisable qui gère la création de comptes, la connexion sécurisée "
        "et les droits d'accès de n'importe quelle application (site web, mobile), avec "
        "réinitialisation de mot de passe par email. Actuellement en ligne et accessible en "
        "démonstration."
    ),
    'hospital': (
        "Application qui permet à une équipe médicale (médecins, infirmiers, administrateurs) "
        "de gérer les dossiers patients en toute sécurité. Chaque action est enregistrée pour "
        "savoir qui a consulté ou modifié quoi, et les comptes sensibles sont protégés par une "
        "double vérification à la connexion."
    ),
}


def apply_descriptions(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, description in DESCRIPTIONS.items():
        Project.objects.filter(slug=slug).update(short_description=description)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_add_more_projects'),
    ]

    operations = [
        migrations.RunPython(apply_descriptions, noop),
    ]
