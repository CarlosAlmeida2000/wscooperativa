# Generated by Django 3.0.8 on 2022-02-01 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_auto_20220201_1359'),
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Usuario.Personas'),
        ),
    ]
