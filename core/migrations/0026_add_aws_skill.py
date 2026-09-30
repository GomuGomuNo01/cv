# Ajoute une compétence "Cloud (AWS)" à la section Outils & Données, en
# cohérence avec les certifications AWS SimuLearn déjà présentes sur le
# portfolio (Les fondamentaux du cloud, Premiers pas dans le cloud).

from django.db import migrations

SKILL = dict(
    category='outils',
    name='Cloud (AWS - fondamentaux)',
    icon_name='cloud',
    order=6,
)


def populate(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.get_or_create(name=SKILL['name'], category=SKILL['category'], defaults=SKILL)


def unpopulate(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.filter(name=SKILL['name'], category=SKILL['category']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_update_education_degrees'),
    ]

    operations = [
        migrations.RunPython(populate, unpopulate),
    ]
