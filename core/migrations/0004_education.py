from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_populate_real_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150)),
                ('degree', models.CharField(help_text='Ex: Master IA & Big Data', max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='education/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, help_text='Laissez vide si en cours', null=True)),
                ('is_current', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Education',
                'ordering': ['-start_date'],
            },
        ),
    ]
