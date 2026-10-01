# Réécrit titre, description et stack technique de tous les projets selon
# la nouvelle structure fournie : phrase d'accroche centrée sur le problème
# métier, puis la solution et un chiffre/preuve de résultat. Les
# technologies ne sont plus mentionnées dans le texte, elles restent
# affichées à part sous forme de tags.
#
# Classe aussi chaque projet dans une catégorie (data / dev) pour que le
# portfolio puisse les afficher en deux sous-sections, et renumérote
# l'ordre d'affichage en conséquence. Le projet career-ops n'est pas
# ajouté (exclusion déjà demandée précédemment, reconfirmée).

from django.db import migrations

# (slug, catégorie, index, titre, description, stack technique)
PROJECTS = [
    (
        'nyc-taxi-data-engineering', 'data', '01',
        'NYC Taxi : où positionner les chauffeurs ?',
        "Une compagnie de taxis veut savoir où et quand positionner ses chauffeurs pour "
        "maximiser leur revenu par heure. L'analyse de 7,7 millions de courses réelles à "
        "New York en 2019 identifie les zones et créneaux les plus rentables et débouche "
        "sur un dashboard Power BI validé par 26 tests automatisés.",
        'Python,PySpark,SQL,Power BI,DAX',
    ),
    (
        'maven-toys-powerbi', 'data', '02',
        'Maven Toys Analytics',
        "Une enseigne de 50 magasins voit son chiffre d'affaires progresser, mais sa marge "
        "se dégrade. L'analyse de 829 262 ventes révèle que les ruptures de stock "
        "représentent un manque à gagner estimé à 29 069 $ par mois, puis transforme ce "
        "constat en recommandations concrètes grâce à un dashboard Power BI.",
        'Power BI,DAX,Power Query,Python',
    ),
    (
        'contoso-sales-powerbi', 'data', '03',
        'Contoso Sales Analytics',
        "Le chiffre d'affaires d'un distributeur recule de 33 % (43,8 M$ à 29,3 M$), sans "
        "explication claire. L'analyse de 225 000 ventes identifie les catégories et "
        "segments les plus touchés, puis restitue le diagnostic à la direction commerciale "
        "dans un dashboard Power BI conçu pour faciliter la prise de décision.",
        'Power BI,DAX,Power Query,Python',
    ),
    (
        'sbs-bank', 'data', '04',
        'SBS Bank',
        "Une néobanque simulée veut vérifier si ses partenaires commerciaux lui apportent "
        "des clients réellement actifs. L'analyse de 254 000 opérations sur 18 mois montre "
        "que les clients issus de ces partenaires utilisent leur compte deux fois moins "
        "souvent que les autres, ce qui permet de formuler six recommandations commerciales "
        "prioritaires.",
        'Python,SQL,Segmentation RFM,Tests statistiques',
    ),
    (
        'telco-churn-prediction', 'data', '05',
        'Telco Churn Prediction',
        "Un opérateur télécom perd des clients chaque mois sans savoir lesquels cibler en "
        "priorité. Après comparaison de neuf modèles sur 7 043 clients, le modèle retenu "
        "détecte 73 % des résiliations réelles et aide l'entreprise à concentrer ses actions "
        "de fidélisation sur les profils les plus à risque.",
        'Python,scikit-learn,Machine Learning',
    ),
    (
        'chatbot-rag-docassist', 'data', '06',
        'Chatbot RAG · DocAssist',
        "Retrouver une information dans des documents internes prend du temps et les "
        "réponses peuvent manquer de fiabilité. DocAssist recherche les passages pertinents, "
        "cite ses sources et indique clairement lorsqu'une information est absente, afin "
        "d'aider les équipes à trouver une réponse vérifiable plus rapidement.",
        'Python,LangChain,FAISS,FastAPI',
    ),
    (
        'sales-report-automation', 'data', '07',
        'Sales Report Automation',
        "Préparer un rapport commercial à la main prend plusieurs heures et augmente le "
        "risque d'erreur. Ce pipeline transforme un fichier CSV brut en un rapport PDF de "
        "six pages en sept secondes, calcule automatiquement les indicateurs clés et "
        "s'appuie sur plus de 50 tests automatisés pour garantir la fiabilité du résultat.",
        'Python,pandas,ReportLab,pytest',
    ),
    (
        'automatisation-de-processus', 'data', '08',
        'Automatisation de processus',
        "Six tâches manuelles (suivi de stock, envoi d'e-mails et collecte de données en "
        "ligne) mobilisent du temps chaque semaine. Ces scripts Python exécutent désormais "
        "les opérations seuls, sont testés avant chaque mise en production et fonctionnent "
        "en service depuis deux ans.",
        'Python,Selenium,Playwright,openpyxl',
    ),
    (
        'hotel-management-system', 'dev', '09',
        'Hotel Management System',
        "Un hôtel doit gérer les réservations, les paiements, les arrivées, les départs et "
        "les réclamations sans créer de conflits entre les informations. Cette application "
        "centralise le cycle de vie des séjours, tandis que les mises à jour sont "
        "immédiatement visibles grâce à la communication en temps réel entre le serveur et "
        "l'interface.",
        'Laravel,React,MySQL,WebSocket',
    ),
    (
        'api-rest-jwt', 'dev', '10',
        'API REST JWT · Spring Boot',
        "Une application métier doit protéger ses données sans devenir difficile à "
        "maintenir. Cette API authentifie chaque utilisateur, applique des droits selon son "
        "rôle et fournit une documentation claire pour faciliter son intégration et son "
        "évolution.",
        'Java,Spring Boot,Spring Security,JUnit,Swagger',
    ),
    (
        'mini-crm-dotnet', 'dev', '11',
        'Mini-CRM',
        "Les informations clients et contrats sont souvent dispersées entre des tableurs et "
        "des e-mails. Cette application centralise leur suivi, restitue les indicateurs clés "
        "dans un tableau de bord et conserve les données dans une base structurée pour "
        "faciliter le pilotage commercial.",
        'C#,ASP.NET Core 8,Entity Framework Core,MySQL',
    ),
    (
        'hospital', 'dev', '12',
        'Hospital',
        "Les données de santé exigent un accès strictement contrôlé et une traçabilité "
        "complète. Ce système sépare les droits entre administrateur, médecin et infirmier, "
        "impose une authentification à deux facteurs et enregistre chaque action dans un "
        "journal d'audit pour renforcer la sécurité.",
        'Laravel,PHP,Blade,MySQL',
    ),
]

OLD_VALUES = {
    'nyc-taxi-data-engineering': dict(
        category='data', index_number='03',
        title='NYC Taxi Data Engineering Pipeline',
        short_description=(
            "Analyse de 7,7 millions de courses de taxis new-yorkais pour déterminer où et "
            "quand positionner les chauffeurs afin de maximiser leur revenu. Les données sont "
            "nettoyées et chaque exclusion est documentée (97 % des données restent "
            "exploitables). Révèle que les aéroports représentent 6 % des courses mais 21 % "
            "du chiffre d'affaires. Dashboard Power BI de 5 pages avec recommandations."
        ),
        tech_stack='PySpark,SQL,Power BI,DAX,Architecture médaillon',
    ),
    'maven-toys-powerbi': dict(
        category='data', index_number='04',
        title='Maven Toys Analytics (Power BI)',
        short_description=(
            "Tableau de bord qui analyse les ventes de 50 magasins d'une enseigne de jouets "
            "(829 262 ventes) et révèle un problème caché : l'entreprise perd 29 069 $ par "
            "mois à cause de ruptures de stock, alors même que son chiffre d'affaires "
            "progresse."
        ),
        tech_stack='Power BI,DAX,Power Query',
    ),
    'contoso-sales-powerbi': dict(
        category='data', index_number='05',
        title='Contoso Sales Analytics (Power BI)',
        short_description=(
            "Tableau de bord qui analyse 225 000 ventes pour comprendre une baisse de "
            "chiffre d'affaires de 33 % (de 43,8 à 29,3 millions de dollars), et identifie "
            "précisément quelles catégories de produits en sont responsables."
        ),
        tech_stack='Power BI,DAX',
    ),
    'sbs-bank': dict(
        category='data', index_number='06',
        title='SBS Bank',
        short_description=(
            "Analyse le comportement de 1 800 clients d'une banque (254 000 opérations) et "
            "révèle que les clients recrutés via des partenaires activent leur compte deux "
            "fois moins souvent que les autres. Propose 6 recommandations concrètes pour "
            "corriger ce problème."
        ),
        tech_stack='SQL,Python,Statistiques',
    ),
    'telco-churn-prediction': dict(
        category='data', index_number='07',
        title='Telco Churn Prediction',
        short_description=(
            "Prédit à l'avance quels clients d'un opérateur télécom risquent de résilier "
            "leur contrat, en comparant 9 méthodes de prédiction sur 7 043 clients. Le "
            "modèle retenu repère un tiers de clients à risque en plus que les méthodes "
            "classiques, pour agir avant leur départ. Accessible via une application en "
            "ligne."
        ),
        tech_stack='Python,scikit-learn,Streamlit',
    ),
    'chatbot-rag-docassist': dict(
        category='data', index_number='01',
        title='Chatbot RAG - DocAssist',
        short_description=(
            "Assistant IA qui répond à des questions posées en langage naturel sur un "
            "ensemble de documents, en citant précisément la source de chaque réponse pour "
            "qu'elle reste vérifiable. Refuse de répondre plutôt que d'inventer une "
            "information absente des documents."
        ),
        tech_stack='Python,RAG,FAISS,LangChain,Streamlit',
    ),
    'sales-report-automation': dict(
        category='data', index_number='10',
        title='Sales Report Automation',
        short_description=(
            "Crée automatiquement un rapport de ventes de 6 pages à partir des données de "
            "l'entreprise, en 7 secondes au lieu de 5 heures si une personne devait le faire "
            "à la main. Plus de 50 tests garantissent que le rapport reste exact à chaque "
            "génération."
        ),
        tech_stack='Python,Automatisation,PDF',
    ),
    'automatisation-de-processus': dict(
        category='data', index_number='09',
        title='Automatisation de processus',
        short_description=(
            "Remplace 6 tâches répétitives qu'un employé ferait à la main : surveiller les "
            "stocks, envoyer une alerte par email en cas de rupture, relever les prix des "
            "concurrents. Fonctionne seul, sans intervention humaine, depuis 2 ans."
        ),
        tech_stack='Python,Selenium,Automatisation',
    ),
    'hotel-management-system': dict(
        category='data', index_number='02',
        title='Système de Gestion Hôtelière',
        short_description=(
            "Application complète de réservation et gestion d'hôtel : catalogue de "
            "chambres, réservations sans conflit de dates, paiements en ligne, suivi en "
            "temps réel des arrivées et départs. Validée par 259 tests automatisés (174 "
            "backend, 85 frontend)."
        ),
        tech_stack='Laravel,React,MySQL,WebSocket',
    ),
    'api-rest-jwt': dict(
        category='dev', index_number='11',
        title='API REST JWT',
        short_description=(
            "Brique technique réutilisable qui gère la création de comptes, la connexion "
            "sécurisée et les droits d'accès de n'importe quelle application (site web, "
            "mobile), avec réinitialisation de mot de passe par email. Actuellement en "
            "ligne et accessible en démonstration."
        ),
        tech_stack='Java,Spring Boot,JWT,MySQL',
    ),
    'mini-crm-dotnet': dict(
        category='dev', index_number='11',
        title='Mini-CRM (.NET)',
        short_description=(
            "Application pour gérer des clients et leurs contrats : création, suivi, "
            "historique. Chaque utilisateur n'a accès qu'aux fonctions liées à son rôle "
            "(administrateur, commercial...), et 52 tests automatisés vérifient que "
            "l'application fonctionne correctement après chaque modification."
        ),
        tech_stack='C#,ASP.NET Core,Entity Framework Core,MySQL',
    ),
    'hospital': dict(
        category='dev', index_number='12',
        title='Hospital',
        short_description=(
            "Application qui permet à une équipe médicale (médecins, infirmiers, "
            "administrateurs) de gérer les dossiers patients en toute sécurité. Chaque "
            "action est enregistrée pour savoir qui a consulté ou modifié quoi, et les "
            "comptes sensibles sont protégés par une double vérification à la connexion."
        ),
        tech_stack='PHP,Laravel,MySQL',
    ),
}


def apply_new(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, category, index, title, description, tech_stack in PROJECTS:
        Project.objects.filter(slug=slug).update(
            category=category, index_number=index, title=title,
            short_description=description, tech_stack=tech_stack,
        )


def revert_old(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    for slug, values in OLD_VALUES.items():
        Project.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_project_category'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
