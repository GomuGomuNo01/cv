# Portfolio — Cédric Kouadio

Portfolio Django (Data Analyst & Développeur).

## Lancer en local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Le site est disponible sur http://localhost:8000/.

Les données du portfolio (compétences, expériences, projets) sont peuplées
automatiquement par la migration `core/migrations/0003_populate_real_data.py`.
