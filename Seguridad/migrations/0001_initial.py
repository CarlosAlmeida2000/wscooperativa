# Generated by Django 3.0.8 on 2022-01-28 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitud_actual', models.FloatField()),
                ('latitud_actual', models.FloatField()),
                ('fecha_hora_alerta', models.DateTimeField()),
                ('ultima_fecha_hora', models.DateTimeField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emergencias', to='Usuario.Personas')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Servicio.Servicios')),
            ],
        ),
        migrations.CreateModel(
            name='ContactosEmergencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_amigo', models.BooleanField(default=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='amigos', to='Usuario.Personas')),
                ('persona_amigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Usuario.Personas')),
            ],
        ),
    ]
