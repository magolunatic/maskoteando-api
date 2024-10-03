# Generated by Django 5.1.1 on 2024-09-26 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='productos.cliente'),
            preserve_default=False,
        ),
    ]