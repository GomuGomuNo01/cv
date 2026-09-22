from django.db import migrations, models

IN_PROGRESS_SLUGS = ['nyc-taxi-data-engineering', 'telco-churn-prediction']


def mark_in_progress(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=IN_PROGRESS_SLUGS).update(in_progress=True)


def unmark_in_progress(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.filter(slug__in=IN_PROGRESS_SLUGS).update(in_progress=False)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_simplify_project_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='in_progress',
            field=models.BooleanField(default=False, help_text='Projet encore en cours de développement'),
        ),
        migrations.RunPython(mark_in_progress, unmark_in_progress),
    ]
