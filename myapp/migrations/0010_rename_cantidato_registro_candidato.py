# Generated by Django 3.2.16 on 2023-10-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20231029_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='cantidato',
            new_name='candidato',
        ),
    ]
