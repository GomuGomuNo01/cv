# Compétences alignées sur la Stack technique du profil GitHub : ajout de Jupyter,
# utilisé pour le notebook d'analyse du projet SBS Bank (Simple-Banking-System-Python).
# Les autres éléments de la Stack figuraient déjà dans cette section.

from django.db import migrations

OLD = 'Python (pandas, NumPy, Matplotlib, Seaborn)'
NEW = 'Python (pandas, NumPy, Matplotlib, Seaborn, Jupyter)'


def apply_new(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.filter(category='data', name=OLD).update(name=NEW)


def revert_old(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.filter(category='data', name=NEW).update(name=OLD)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_linkedin_experience_and_hide_projects'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
