# Portfolio · Cédric Kouadio

Portfolio Django (Data Analyst & Développeur).

## Lancer en local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Le site est disponible sur http://localhost:8000/.

Les données du portfolio (compétences, expériences, projets) sont peuplées
automatiquement par les migrations de `core/migrations/`.

## Déployer sur Render

Ce repo contient un `render.yaml` (Blueprint Render) qui configure tout
automatiquement : build, migrations, variable `SECRET_KEY` générée, et
détection du nom d'hôte public.

1. Sur [render.com](https://render.com), New + → **Blueprint**.
2. Connecter ce repo GitHub (`GomuGomuNo01/cv`).
3. Render détecte `render.yaml` et propose le service `cedric-kouadio-portfolio`.
   Vérifier le plan **Free**, puis **Apply**.
4. Premier déploiement : quelques minutes (installation, `collectstatic`,
   `migrate`). L'URL publique est du type
   `https://cedric-kouadio-portfolio.onrender.com`.

### À savoir avant de déployer

- **Base de données éphémère** : ce projet utilise SQLite, recréée à
  chaque déploiement à partir des migrations (c'est voulu : tout le
  contenu du portfolio est versionné dans le code, pas saisi à la main).
  Toute modification faite en direct via `/admin/` sur le site en ligne
  sera donc perdue au prochain déploiement, sauf ajout d'un disque
  persistant ou d'une vraie base de données (services payants sur Render).
- **Plan gratuit** : le service s'endort après une période d'inactivité
  et met quelques dizaines de secondes à redémarrer au premier accès.
