# Ajoute le détail des missions (une par ligne) pour chaque expérience,
# affiché dans le menu déroulant de la section "Expérience Professionnelle".
# Contenu repris du profil LinkedIn du titulaire.

from django.db import migrations

TASKS = {
    'IT-CENTREX': (
        "Développement d'applications web avec Java / Spring Boot et mobiles avec Flutter, "
        "de la conception à la mise en production.\n"
        "Conception et documentation d'API REST sécurisées avec JWT et Swagger, testées avec "
        "Postman.\n"
        "Création d'un assistant IA sur les documents internes, avec plus de 85 % de réponses "
        "correctes en moins de 2 secondes.\n"
        "Mise en place de modèles de classification automatique pour analyser et catégoriser "
        "des documents et des rapports destinés aux équipes Finance et Opérations.\n"
        "Déploiement d'un pipeline ETL et de rapports automatisés générés en 7 secondes, "
        "utilisé en production sans incident depuis le lancement.\n"
        "Conception de maquettes d'interfaces sur Figma en collaboration avec les équipes "
        "métier.\n"
        "Supervision des applications en production, suivi des incidents et rédaction de la "
        "documentation technique.\n"
        "Résultat : des applications et services IA déployés en production, des processus "
        "documentaires automatisés et des rapports générés plus rapidement pour les équipes "
        "internes."
    ),
    'madameb0nplan': (
        "Fiabilisation des bases de données SQL : nettoyage, modélisation et mise en place de "
        "contrôles qualité réguliers.\n"
        "Automatisation de la collecte et du traitement des données avec Python (pandas), pour "
        "supprimer les manipulations manuelles répétitives.\n"
        "Conception de tableaux de bord Power BI (modèle en étoile, mesures DAX) pour suivre "
        "les indicateurs clés de l'activité.\n"
        "Analyse des résultats et restitution des tendances à l'équipe pour appuyer les "
        "décisions.\n"
        "Résultat : des données fiables et des indicateurs à jour, consultables par l'équipe "
        "sans retraitement manuel."
    ),
    'African Business Club (ABC)': (
        "Structuration des besoins data du pôle (membres, événements et partenaires) et "
        "définition de règles de saisie communes pour harmoniser les informations.\n"
        "Fiabilisation des bases de contacts et d'adhérents : dédoublonnage, nettoyage des "
        "données et contrôles de cohérence réguliers.\n"
        "Conception de tableaux de bord légers avec Excel et Power BI pour suivre l'activité "
        "du club, les participations et les tendances clés.\n"
        "Automatisation d'une partie de la collecte et du traitement des données avec Python "
        "et Excel avancé afin de réduire les saisies manuelles.\n"
        "Développement de scripts Python avec pandas et openpyxl pour nettoyer, transformer et "
        "enrichir les fichiers internes.\n"
        "Mise en place de requêtes SQL et de formules Excel avancées pour consolider les "
        "données et alimenter les indicateurs du pôle.\n"
        "Documentation des jeux de données, des indicateurs et des procédures de mise à jour "
        "afin de faciliter l'utilisation des outils par les membres non techniques.\n"
        "Résultat : des données mieux structurées et plus fiables, des indicateurs plus "
        "facilement accessibles et des processus de suivi progressivement simplifiés pour les "
        "équipes du club."
    ),
    'Institut Pasteur de Côte d’Ivoire': (
        "Développement d'une application web avec Java / Spring Boot pour centraliser et "
        "protéger les données médicales.\n"
        "Mise en place d'une gestion des accès par rôle afin de contrôler les droits des "
        "utilisateurs selon leurs responsabilités.\n"
        "Implémentation d'un mécanisme de traçabilité des actions pour renforcer la "
        "confidentialité et faciliter les contrôles.\n"
        "Administration des bases de données MySQL et SQL Server : extraction, mise à jour et "
        "contrôle de la fiabilité des données patients.\n"
        "Résultat : données médicales centralisées et mieux protégées, accès utilisateurs "
        "contrôlés par rôle et actions tracées pour renforcer la confidentialité."
    ),
    'AIDE JEUNES': (
        "Formation des utilisateurs aux fonctionnalités des logiciels et accompagnement dans "
        "leur utilisation quotidienne.\n"
        "Diagnostic et résolution des incidents techniques rencontrés par les équipes.\n"
        "Rédaction de guides utilisateurs clairs pour faciliter l'appropriation des outils et "
        "réduire les sollicitations récurrentes.\n"
        "Collecte et analyse des retours utilisateurs afin d'identifier les besoins "
        "d'amélioration des logiciels.\n"
        "Résultat : utilisateurs mieux accompagnés, documentation accessible et résolution "
        "plus rapide des problèmes rencontrés au quotidien."
    ),
    'TASNIM SOLUTION': (
        "Développement d'une application web de gestion des utilisateurs et de leurs droits "
        "d'accès aux données internes avec Laravel et PHP.\n"
        "Conception d'une solution de paiement commune pour centraliser les transactions des "
        "différentes plateformes de l'entreprise.\n"
        "Développement d'un outil de bureau en C# pour automatiser les tâches administratives "
        "répétitives et réduire les erreurs de saisie.\n"
        "Résultat : gestion des accès centralisée, processus de paiement harmonisés et tâches "
        "administratives simplifiées grâce à l'automatisation."
    ),
}

OLD_DESCRIPTIONS = {
    'madameb0nplan': (
        "Automatisation de la collecte de données via des scripts Python, "
        "fiabilisation de bases SQL via nettoyage et contrôles qualité, "
        "alimentation de tableaux de bord Power BI restitués quotidiennement à l'équipe."
    ),
    'IT-CENTREX': (
        "Conception de modèles de détection d'anomalies (scikit-learn), "
        "développement d'API REST (Java, Python) connectant plusieurs systèmes existants, "
        "fiabilisation de traitements de données répétitifs."
    ),
    'TASNIM SOLUTION': (
        "Développement d'applications web avec Laravel (MVC, ORM Eloquent) "
        "et d'une application C# d'automatisation."
    ),
    'Institut Pasteur de Côte d’Ivoire': (
        "Conception et administration de bases de données relationnelles "
        "(MySQL, SQL Server) via modélisation et migration, développement d'une "
        "application interne utilisée par du personnel non technique."
    ),
    'African Business Club (ABC)': '',
    'AIDE JEUNES': '',
}


def apply_new(apps, schema_editor):
    Company = apps.get_model('core', 'Company')
    for name, description in TASKS.items():
        Company.objects.filter(name=name).update(description=description)


def revert_old(apps, schema_editor):
    Company = apps.get_model('core', 'Company')
    for name, description in OLD_DESCRIPTIONS.items():
        Company.objects.filter(name=name).update(description=description)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_project_copy_rewrite'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
