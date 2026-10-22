# Section Expérience alignée sur l'onglet "Expérience" du profil LinkedIn
# (relevé le 22/10/2026) : nouveaux intitulés (ABC : "Data Engineer &
# Développeur Fullstack"), tâches reformulées au passé pour les postes
# terminés, avec les chiffres publiés sur LinkedIn. Comme précédemment, le
# portfolio n'affiche que les tâches (pas l'introduction ni la ligne "Outils").

from django.db import migrations

# (nom, nouvel intitulé, nouvelles tâches, ancien intitulé, anciennes tâches)
EXPERIENCES = [
    (
        "African Business Club (ABC)",
        "Data Engineer & Développeur Fullstack",
        "Dédoublonne et nettoie plus de 100 enregistrements des bases de membres, d'événements et de partenaires, avec des contrôles de cohérence réguliers et des règles de saisie communes qui harmonisent les informations.\nAutomatise le nettoyage, la transformation et l'enrichissement des fichiers internes avec des scripts Python (pandas, openpyxl), pour un traitement en moins de 10 minutes au lieu de 3 heures.\nAnalyse les participations et les tendances du club avec SQL et Excel avancé, puis publie des tableaux de bord Power BI (mesures DAX) et Google Sheets, consultés par les membres des autres pôles pour appuyer les décisions du pôle.\nDéveloppe des interfaces web responsive en React, TypeScript et Tailwind CSS, connectées à une API FastAPI (JSON) et à des requêtes SQL, et les améliore à partir des retours des membres.\nLivre des évolutions fiables grâce aux tests automatisés (pytest), à Git et aux relectures de code sur GitHub, et documente les jeux de données, les indicateurs et les procédures de mise à jour pour les membres non techniques.",
        "Data Scientist & Développeur Fullstack",
        "Structuration des besoins data du pôle : membres, événements et partenaires ; définition de règles de saisie communes pour harmoniser les informations.\nFiabilisation des bases de contacts et d'adhérents : dédoublonnage, nettoyage des données et contrôles de cohérence réguliers.\nDéveloppement de scripts Python avec pandas et openpyxl pour nettoyer, transformer et enrichir les fichiers internes avant analyse.\nAnalyse des participations et des tendances du club avec SQL et Excel avancé, afin d'appuyer les décisions du pôle.\nConception de tableaux de bord de suivi avec Power BI (mesures DAX) et Google Sheets, lisibles par tous.\nDéveloppement d'interfaces web responsive avec React, TypeScript et Tailwind CSS, et de composants réutilisables pour harmoniser les pages et accélérer les évolutions.\nConnexion des interfaces aux données via une API FastAPI au format JSON et des requêtes SQL, pour des écrans de suivi toujours à jour.\nAmélioration de la lisibilité et de l'ergonomie des écrans à partir des retours des membres.\nMise en place de tests automatisés (pytest), suivi des versions avec Git et relectures de code entre membres sur GitHub, pour livrer des évolutions fiables.\nDocumentation des jeux de données, des indicateurs et des procédures de mise à jour pour faciliter l'utilisation des outils par les membres non techniques.\nRésultat : des données plus fiables, des indicateurs accessibles à tous et des interfaces de suivi plus claires, fiables et faciles à faire évoluer pour les équipes du club.",
    ),
    (
        "madameb0nplan",
        "Data Analyst",
        "Analysa l'activité et présenta les tendances à l'équipe avec des indicateurs clés (chiffre d'affaires brut et net, panier moyen, taux d'annulation), pour appuyer les décisions.\nNettoya et modélisa les bases SQL avec des contrôles qualité réguliers, sur plusieurs jeux de données : 7,7 millions de trajets, 225 000 ventes et 254 000 transactions sur 18 mois.\nAutomatisa la collecte et le traitement des données avec Python (pandas, numpy), sans manipulation manuelle : gain estimé de 25 minutes par jour, soit environ 83 % du temps consacré à cette tâche.\nConçut des tableaux de bord Power BI (modèle en étoile, mesures DAX), toujours à jour sans retraitement manuel, consultés par le département marketing et d'autres départements.",
        "Data Analyst",
        "Analyse des résultats et restitution des tendances à l'équipe, avec des indicateurs clés pour appuyer les décisions.\nFiabilisation des bases SQL : nettoyage, modélisation et contrôles qualité réguliers pour des chiffres exploitables.\nAutomatisation de la collecte et du traitement des données avec Python (pandas, numpy), sans manipulation manuelle.\nConception de tableaux de bord Power BI (modèle en étoile, mesures DAX) pour suivre les indicateurs clés de l'activité.\nTableaux de bord toujours à jour, consultables par l'équipe sans retraitement manuel.\nRésultat : des données fiables et des indicateurs à jour, accessibles à toute l'équipe sans retraitement manuel.",
    ),
    (
        "IT Centrex",
        "Développeur Full-Stack & IA",
        "Créa un assistant IA sur les documents internes : plus de 85 % de réponses jugées correctes lors de tests internes, en moins de 2 secondes.\nDéploya un pipeline ETL qui génère des rapports automatisés en 7 secondes, au lieu de 2 h 30 de traitement manuel, sur des volumes de plusieurs centaines de milliers à plusieurs millions d'enregistrements, en production sans incident depuis le lancement.\nMit en place, avec Python (scikit-learn), des modèles de classification automatique de documents et de rapports pour les équipes Finance et Opérations, évalués par le taux de bonnes prédictions sur un jeu de test indépendant de l'entraînement.\nDéveloppa des applications web (Java / Spring Boot) et mobiles (Flutter) reliées à des API REST sécurisées (JWT, Swagger), documentées et testées avec Postman, de la conception à la mise en production.\nAssura la supervision des applications en production, le suivi des incidents et la rédaction de la documentation technique, et conçut des maquettes d'interfaces sur Figma en collaboration avec les équipes métier.",
        "Développeur Full-Stack & IA",
        "Développement d'applications web avec Java / Spring Boot et mobiles avec Flutter, de la conception à la mise en production.\nConception et documentation d'API REST sécurisées avec JWT et Swagger, testées avec Postman.\nCréation d'un assistant IA sur les documents internes, avec plus de 85 % de réponses correctes en moins de 2 secondes.\nMise en place de modèles de classification automatique pour analyser et catégoriser des documents et des rapports destinés aux équipes Finance et Opérations.\nDéploiement d'un pipeline ETL et de rapports automatisés générés en 7 secondes, utilisé en production sans incident depuis le lancement.\nConception de maquettes d'interfaces sur Figma en collaboration avec les équipes métier.\nSupervision des applications en production, suivi des incidents et rédaction de la documentation technique.\nRésultat : des applications et services IA déployés en production, des processus documentaires automatisés et des rapports générés plus rapidement pour les équipes internes.",
    ),
    (
        "TASNIME SOLUTION",
        "Développeur Full-Stack",
        "Développa une application web Laravel / PHP de gestion des utilisateurs et de leurs droits d'accès aux données internes, pour plus de 40 utilisateurs.\nConçut une solution de paiement commune qui centralise les transactions de 5 plateformes de l'entreprise.\nAutomatisa des tâches administratives répétitives avec un outil de bureau en C#, ce qui réduisit les erreurs de saisie de 90 %.",
        "Développeur Full-Stack",
        "Développement d'une application web de gestion des utilisateurs et de leurs droits d'accès aux données internes avec Laravel et PHP.\nConception d'une solution de paiement commune pour centraliser les transactions des différentes plateformes de l'entreprise.\nDéveloppement d'un outil de bureau en C# pour automatiser les tâches administratives répétitives et réduire les erreurs de saisie.\nRésultat : gestion des accès centralisée, processus de paiement harmonisés et tâches administratives simplifiées grâce à l'automatisation.",
    ),
    (
        "AIDE JEUNES",
        "Support Technique & Formateur",
        "Forma plus de 30 utilisateurs aux logiciels de la structure et les accompagna dans leur usage quotidien.\nDiagnostiqua et résolut plus de 15 incidents techniques des équipes.\nRédigea des guides utilisateurs pour faciliter l'appropriation des outils et réduire les sollicitations répétitives.\nCollecta et analysa les retours des utilisateurs pour identifier les améliorations des logiciels.",
        "Support Technique & Formateur",
        "Formation des utilisateurs aux fonctionnalités des logiciels et accompagnement dans leur utilisation quotidienne.\nDiagnostic et résolution des incidents techniques rencontrés par les équipes.\nRédaction de guides utilisateurs clairs pour faciliter l'appropriation des outils et réduire les sollicitations récurrentes.\nCollecte et analyse des retours utilisateurs afin d'identifier les besoins d'amélioration des logiciels.\nRésultat : utilisateurs mieux accompagnés, documentation accessible et résolution plus rapide des problèmes rencontrés au quotidien.",
    ),
    (
        "Institut Pasteur de Côte d’Ivoire",
        "Développeur Full-Stack",
        "Développa une application web Java / Spring Boot qui centralise et protège des données médicales sensibles, pour plus de 100 utilisateurs et dossiers.\nMit en place une gestion des accès par rôle pour contrôler les droits selon les responsabilités.\nImplémenta un mécanisme de traçabilité des actions pour renforcer la confidentialité et faciliter les contrôles.\nAdministra les bases MySQL et SQL Server : extraction, mise à jour et contrôle de la fiabilité de centaines à plusieurs milliers d'enregistrements patients.",
        "Développeur Full-Stack",
        "Développement d'une application web avec Java / Spring Boot pour centraliser et protéger les données médicales.\nMise en place d'une gestion des accès par rôle afin de contrôler les droits des utilisateurs selon leurs responsabilités.\nImplémentation d'un mécanisme de traçabilité des actions pour renforcer la confidentialité et faciliter les contrôles.\nAdministration des bases de données MySQL et SQL Server : extraction, mise à jour et contrôle de la fiabilité des données patients.\nRésultat : données médicales centralisées et mieux protégées, accès utilisateurs contrôlés par rôle et actions tracées pour renforcer la confidentialité.",
    ),
]


def _appliquer(apps, nouveau):
    Company = apps.get_model('core', 'Company')
    for nom, titre, taches, ancien_titre, anciennes_taches in EXPERIENCES:
        valeurs = (
            dict(job_title=titre, description=taches) if nouveau
            else dict(job_title=ancien_titre, description=anciennes_taches)
        )
        Company.objects.filter(name=nom).update(**valeurs)


def apply_new(apps, schema_editor):
    _appliquer(apps, True)


def revert_old(apps, schema_editor):
    _appliquer(apps, False)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_skill_jupyter'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
