from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_hotel_management_second_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='download_link',
            field=models.URLField(blank=True, help_text='Lien de téléchargement direct (ex: rapport .pbix)'),
        ),
        migrations.AddField(
            model_name='project',
            name='download_label',
            field=models.CharField(blank=True, help_text='Ex: .pbix avec données', max_length=60),
        ),
    ]
