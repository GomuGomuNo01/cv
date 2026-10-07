# Chatbot RAG · DocAssist : nouveau texte fourni par le titulaire.

from django.db import migrations

SLUG = 'chatbot-rag-docassist'

NEW_DESCRIPTION = (
    "Un assistant IA qui transforme les documents internes en réponses rapides et "
    "vérifiables. Il retrouve les informations pertinentes, cite ses sources et signale "
    "lorsqu’une réponse est absente. Objectif : gagner du temps tout en renforçant la "
    "fiabilité des réponses."
)

OLD_DESCRIPTION = (
    "Retrouver une information dans des documents internes prend du temps et les "
    "réponses peuvent manquer de fiabilité. DocAssist recherche les passages pertinents, "
    "cite ses sources et indique clairement lorsqu'une information est absente, afin "
    "d'aider les équipes à trouver une réponse vérifiable plus rapidement."
)


def apply_new(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=NEW_DESCRIPTION)


def revert_old(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug=SLUG).update(short_description=OLD_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_iuc_presentation_video'),
    ]

    operations = [
        migrations.RunPython(apply_new, revert_old),
    ]
