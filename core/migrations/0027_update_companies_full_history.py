# Met à jour l'historique professionnel complet (intitulés de poste et
# dates de fin actualisés, deux nouvelles expériences) suite à la liste
# fournie par le titulaire. Les missions détaillées existantes ne sont pas
# affichées dans la section "Expérience Professionnelle" du portfolio (poste
# / entreprise / lieu / période uniquement), donc aucune tâche n'est
# inventée pour les deux nouvelles entrées.

from datetime import date

from django.db import migrations

# (nom, lieu, intitulé, début, fin, poste actuel)
NEW_COMPANIES = [
    ('African Business Club (ABC)', 'Paris, France',
     'Data Analyst & Développeur - Pôle IT & Data',
     date(2026, 9, 1), None, True),
    ('AIDE JEUNES', 'Abidjan, Côte d’Ivoire',
     'Support Technique & Formateur',
     date(2023, 9, 1), date(2023, 12, 31), False),
]

# Mises à jour de poste / date de fin sur des entreprises déjà présentes
# (la description existante n'est pas touchée, elle n'est simplement plus
# affichée sur le site).
UPDATED_COMPANIES = {
    'IT-CENTREX': dict(job_title='Développeur Full-Stack & IA', end_date=date(2025, 10, 31)),
    'TASNIM SOLUTION': dict(job_title='Développeur Web Backend (PHP, Laravel)', end_date=date(2024, 6, 30)),
    'Institut Pasteur de Côte d’Ivoire': dict(job_title='Développeur Web Java', end_date=date(2023, 12, 31)),
}

OLD_VALUES = {
    'IT-CENTREX': dict(job_title='Développeur (Python & IA)', end_date=date(2025, 8, 31)),
    'TASNIM SOLUTION': dict(job_title='Stagiaire Développeur', end_date=date(2024, 4, 30)),
    'Institut Pasteur de Côte d’Ivoire': dict(job_title='Stagiaire Développeur', end_date=date(2023, 7, 31)),
}


def apply_new(apps, schema_editor):
    Company = apps.get_model('core', 'Company')

    for name, location, job_title, start, end, is_current in NEW_COMPANIES:
        Company.objects.get_or_create(
            name=name,
            defaults=dict(
                location=location, job_title=job_title,
                start_date=start, end_date=end, is_current=is_current,
                description='',
            ),
        )

    for name, values in UPDATED_COMPANIES.items():
        Company.objects.filter(name=name).update(**values)


def revert_old(apps, schema_editor):
    Company = apps.get_model('core', 'Company')
    Company.objects.filter(name__in=[c[0] for c in NEW_COMPANIES]).delete()
    for name, values in OLD_VALUES.items():
        Company.objects.filter(name=name).update(**values)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_add_aws_skill'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
