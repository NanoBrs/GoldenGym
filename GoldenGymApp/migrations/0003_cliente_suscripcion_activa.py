# Generated by Django 3.2 on 2024-11-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenGymApp', '0002_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='suscripcion_activa',
            field=models.BooleanField(default=False),
        ),
    ]
