# Place en tête de la section Projets (Data & IA) les trois projets avec
# vidéo de présentation, dans l'ordre demandé : Chatbot RAG · DocAssist,
# Instagram Unlike Cleaner, Sales Report Automation. Les autres suivent dans
# leur ordre précédent ; la section Développement ne change pas.

from django.db import migrations

NEW_ORDER = [
    ('chatbot-rag-docassist', '01'),
    ('instagram-unlike-cleaner', '02'),
    ('sales-report-automation', '03'),
    ('nyc-taxi-data-engineering', '04'),
    ('maven-toys-powerbi', '05'),
    ('contoso-sales-powerbi', '06'),
    ('sbs-bank', '07'),
    ('telco-churn-prediction', '08'),
    ('automatisation-de-processus', '09'),
]

OLD_ORDER = [
    ('nyc-taxi-data-engineering', '01'),
    ('maven-toys-powerbi', '02'),
    ('contoso-sales-powerbi', '03'),
    ('sbs-bank', '04'),
    ('telco-churn-prediction', '05'),
    ('chatbot-rag-docassist', '06'),
    ('sales-report-automation', '07'),
    ('automatisation-de-processus', '08'),
    ('instagram-unlike-cleaner', '09'),
]


def apply_order(order):
    def run(apps, schema_editor):
        Project = apps.get_model('core', 'Project')
        for slug, index in order:
            Project.objects.filter(slug=slug).update(index_number=index)
    return run


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_sales_report_video_and_iuc_data'),
    ]

    operations = [
        migrations.RunPython(apply_order(NEW_ORDER), apply_order(OLD_ORDER)),
    ]
