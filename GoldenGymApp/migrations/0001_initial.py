# Generated by Django 3.2 on 2024-11-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('membresia', models.CharField(choices=[('SEMANAL', 'Semanal - $15,000'), ('MENSUAL', 'Mensual - $28,000'), ('TRIMESTRAL', 'Trimestral - $75,000'), ('SEMESTRAL', 'Semestral - $135,000')], max_length=10)),
            ],
        ),
    ]