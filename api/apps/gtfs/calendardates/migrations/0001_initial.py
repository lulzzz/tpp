# Generated by Django 2.0 on 2018-02-15 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('exception_type', models.IntegerField(choices=[(1, 'Serviço adicionado'), (2, 'Serviço removido')])),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='calendardates', to='services.Service')),
            ],
        ),
    ]
