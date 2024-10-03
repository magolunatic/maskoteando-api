# Generated by Django 5.1.1 on 2024-09-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ci', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=255)),
                ('barrio', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]