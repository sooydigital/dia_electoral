# Generated by Django 3.2.16 on 2023-10-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_cantidato_registro_candidato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='numero_de_votos',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
