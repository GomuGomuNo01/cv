# Compétences mises à jour d'après le dépôt monthimmo-cas-pratique : workflow n8n
# de 17 étapes, tableau Airtable, lecture d'emails par Claude Haiku (température 0),
# alertes Gmail (IMAP / SMTP), gestion des doublons et des pannes.

from django.db import migrations

OLD_CLAUDE = 'API Claude (Anthropic), prompt engineering'
NEW_CLAUDE = 'API Claude (Anthropic, Haiku), extraction de données, prompt engineering'
NEW_SKILL = ('ia', 'Workflows automatisés (n8n, Airtable, Gmail IMAP / SMTP)', 'account_tree', 7)


def apply_new(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.filter(category='ia', name=OLD_CLAUDE).update(name=NEW_CLAUDE)
    c, n, i, o = NEW_SKILL
    Skill.objects.get_or_create(category=c, name=n, defaults={'icon_name': i, 'order': o})


def revert_old(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    Skill.objects.filter(category='ia', name=NEW_CLAUDE).update(name=OLD_CLAUDE)
    Skill.objects.filter(category=NEW_SKILL[0], name=NEW_SKILL[1]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_site_amid_texte'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
