# Generated by Django 3.2.9 on 2021-11-12 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedores',
            old_name='Ciudad_proveedor',
            new_name='ciudad_proveedor',
        ),
        migrations.RenameField(
            model_name='proveedores',
            old_name='Direccion_proveedor',
            new_name='direccion_proveedor',
        ),
        migrations.RenameField(
            model_name='proveedores',
            old_name='Nombre_proveedor',
            new_name='nombre_proveedor',
        ),
        migrations.RenameField(
            model_name='proveedores',
            old_name='Telefono_proveedor',
            new_name='telefono_proveedor',
        ),
    ]