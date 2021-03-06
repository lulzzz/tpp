# Generated by Django 2.0 on 2018-02-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'agencies'},
        ),
        migrations.AddField(
            model_name='agency',
            name='timezone',
            field=models.CharField(default='Europe/Lisbon', help_text='Timezone da opderadora de transportes', max_length=255),
        ),
        migrations.AddField(
            model_name='agency',
            name='url',
            field=models.URLField(blank=True, help_text='URL da operadora de transportes'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(db_index=True, help_text='Nome completo da operadora de transportes', max_length=50),
        ),
    ]
