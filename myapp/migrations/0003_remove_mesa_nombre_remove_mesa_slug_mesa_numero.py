# Generated by Django 4.2.6 on 2023-10-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_positive_integer_field_registro_numero_de_votos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='slug',
        ),
        migrations.AddField(
            model_name='mesa',
            name='numero',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
