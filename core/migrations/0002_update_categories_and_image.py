# Generated manually to match the updated Skill categories and the
# optional Project.image field (see core/models.py).

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(
                choices=[
                    ('data', 'Data'),
                    ('ia', 'IA & Automatisation'),
                    ('dev', 'Développement'),
                    ('outils', 'Outils & Données'),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
    ]
