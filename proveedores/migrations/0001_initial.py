# Generated by Django 3.2.9 on 2021-11-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('Nit', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_proveedor', models.CharField(max_length=255, null=True)),
                ('Direccion_proveedor', models.CharField(max_length=255, null=True)),
                ('Telefono_proveedor', models.CharField(max_length=255, null=True)),
                ('Ciudad_proveedor', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]