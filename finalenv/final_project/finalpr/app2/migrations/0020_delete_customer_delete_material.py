# Generated by Django 4.2.2 on 2023-11-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0019_material_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
