# 1) Hospital et Telco Churn Prediction ne sont plus affichés (is_featured
#    passe à False : les données restent en base). Les projets suivants sont
#    renumérotés pour garder une suite continue.
# 2) Section Expérience alignée sur l'onglet "Expérience" du profil LinkedIn
#    (relevé le 16/10/2026) : intitulés, noms d'entreprise, lieux, puces et
#    ligne "Résultat". Le texte d'introduction et la ligne "Outils" propres à
#    LinkedIn ne sont pas repris : le portfolio n'affiche que les tâches.

from django.db import migrations

HIDDEN = ['hospital', 'telco-churn-prediction']

# (slug, nouveau numéro, ancien numéro)
RENUMBER = [
    ('automatisation-de-processus', '08', '09'),
    ('hotel-management-system', '09', '10'),
    ('api-rest-jwt', '10', '11'),
    ('mini-crm-dotnet', '11', '12'),
]

# clé = ancien nom ; valeurs = (nouvelles, anciennes)
EXPERIENCES = {
    'African Business Club (ABC)': (
        dict(
            name='African Business Club (ABC)',
            job_title='Data Scientist & Développeur Fullstack',
            location='Paris, France',
            description="\n".join([
                "Structuration des besoins data du pôle : membres, événements et partenaires ; définition de règles de saisie communes pour harmoniser les informations.",
                "Fiabilisation des bases de contacts et d'adhérents : dédoublonnage, nettoyage des données et contrôles de cohérence réguliers.",
                "Développement de scripts Python avec pandas et openpyxl pour nettoyer, transformer et enrichir les fichiers internes avant analyse.",
                "Analyse des participations et des tendances du club avec SQL et Excel avancé, afin d'appuyer les décisions du pôle.",
                "Conception de tableaux de bord de suivi avec Power BI (mesures DAX) et Google Sheets, lisibles par tous.",
                "Développement d'interfaces web responsive avec React, TypeScript et Tailwind CSS, et de composants réutilisables pour harmoniser les pages et accélérer les évolutions.",
                "Connexion des interfaces aux données via une API FastAPI au format JSON et des requêtes SQL, pour des écrans de suivi toujours à jour.",
                "Amélioration de la lisibilité et de l'ergonomie des écrans à partir des retours des membres.",
                "Mise en place de tests automatisés (pytest), suivi des versions avec Git et relectures de code entre membres sur GitHub, pour livrer des évolutions fiables.",
                "Documentation des jeux de données, des indicateurs et des procédures de mise à jour pour faciliter l'utilisation des outils par les membres non techniques.",
                "Résultat : des données plus fiables, des indicateurs accessibles à tous et des interfaces de suivi plus claires, fiables et faciles à faire évoluer pour les équipes du club.",
            ]),
        ),
        dict(
            name='African Business Club (ABC)',
            job_title='Data Analyst & Développeur - Pôle IT & Data',
            location='Paris, France',
            description="\n".join([
                "Structuration des besoins data du pôle (membres, événements et partenaires) et définition de règles de saisie communes pour harmoniser les informations.",
                "Fiabilisation des bases de contacts et d'adhérents : dédoublonnage, nettoyage des données et contrôles de cohérence réguliers.",
                "Conception de tableaux de bord légers avec Excel et Power BI pour suivre l'activité du club, les participations et les tendances clés.",
                "Automatisation d'une partie de la collecte et du traitement des données avec Python et Excel avancé afin de réduire les saisies manuelles.",
                "Développement de scripts Python avec pandas et openpyxl pour nettoyer, transformer et enrichir les fichiers internes.",
                "Mise en place de requêtes SQL et de formules Excel avancées pour consolider les données et alimenter les indicateurs du pôle.",
                "Documentation des jeux de données, des indicateurs et des procédures de mise à jour afin de faciliter l'utilisation des outils par les membres non techniques.",
                "Résultat : des données mieux structurées et plus fiables, des indicateurs plus facilement accessibles et des processus de suivi progressivement simplifiés pour les équipes du club.",
            ]),
        ),
    ),
    'madameb0nplan': (
        dict(
            name='madameb0nplan',
            job_title='Data Analyst',
            location='Paris, France',
            description="\n".join([
                "Analyse des résultats et restitution des tendances à l'équipe, avec des indicateurs clés pour appuyer les décisions.",
                "Fiabilisation des bases SQL : nettoyage, modélisation et contrôles qualité réguliers pour des chiffres exploitables.",
                "Automatisation de la collecte et du traitement des données avec Python (pandas, numpy), sans manipulation manuelle.",
                "Conception de tableaux de bord Power BI (modèle en étoile, mesures DAX) pour suivre les indicateurs clés de l'activité.",
                "Tableaux de bord toujours à jour, consultables par l'équipe sans retraitement manuel.",
                "Résultat : des données fiables et des indicateurs à jour, accessibles à toute l'équipe sans retraitement manuel.",
            ]),
        ),
        dict(
            name='madameb0nplan',
            job_title='Stagiaire Data Analyst',
            location='Paris, France',
            description="\n".join([
                "Fiabilisation des bases de données SQL : nettoyage, modélisation et mise en place de contrôles qualité réguliers.",
                "Automatisation de la collecte et du traitement des données avec Python (pandas), pour supprimer les manipulations manuelles répétitives.",
                "Conception de tableaux de bord Power BI (modèle en étoile, mesures DAX) pour suivre les indicateurs clés de l'activité.",
                "Analyse des résultats et restitution des tendances à l'équipe pour appuyer les décisions.",
                "Résultat : des données fiables et des indicateurs à jour, consultables par l'équipe sans retraitement manuel.",
            ]),
        ),
    ),
    'IT-CENTREX': (
        dict(
            name='IT Centrex',
            job_title='Développeur Full-Stack & IA',
            location='Abidjan, Côte d’Ivoire',
            description=None,  # inchangée : déjà identique à LinkedIn
        ),
        dict(
            name='IT-CENTREX',
            job_title='Développeur Full-Stack & IA',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
    ),
    'TASNIM SOLUTION': (
        dict(
            name='TASNIME SOLUTION',
            job_title='Développeur Full-Stack',
            location='Abidjan, Côte d’Ivoire',
            description=None,  # puces identiques ; la ligne "Outils" n'est pas reprise
        ),
        dict(
            name='TASNIM SOLUTION',
            job_title='Développeur Web Backend (PHP, Laravel)',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
    ),
    'AIDE JEUNES': (
        dict(
            name='AIDE JEUNES',
            job_title='Support Technique & Formateur',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
        dict(
            name='AIDE JEUNES',
            job_title='Support Technique & Formateur',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
    ),
    'Institut Pasteur de Côte d’Ivoire': (
        dict(
            name='Institut Pasteur de Côte d’Ivoire',
            job_title='Développeur Full-Stack',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
        dict(
            name='Institut Pasteur de Côte d’Ivoire',
            job_title='Développeur Web Java',
            location='Abidjan, Côte d’Ivoire',
            description=None,
        ),
    ),
}


def _set_experiences(apps, index):
    Company = apps.get_model('core', 'Company')
    for key, versions in EXPERIENCES.items():
        # on retrouve la ligne par l'un ou l'autre des deux noms possibles
        company = Company.objects.filter(name__in=[versions[0]['name'], versions[1]['name']]).first()
        if not company:
            continue
        values = {k: v for k, v in versions[index].items() if v is not None}
        Company.objects.filter(pk=company.pk).update(**values)


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=HIDDEN).update(is_featured=False)
    for slug, new, _old in RENUMBER:
        Project.objects.filter(slug=slug).update(index_number=new)
    _set_experiences(apps, 0)


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, _new, old in reversed(RENUMBER):
        Project.objects.filter(slug=slug).update(index_number=old)
    Project.objects.filter(slug__in=HIDDEN).update(is_featured=True)
    _set_experiences(apps, 1)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_contoso_text'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
