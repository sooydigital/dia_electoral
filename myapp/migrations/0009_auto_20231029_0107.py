# Generated by Django 3.2.16 on 2023-10-29 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_candidato_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='puesto_votacion',
        ),
        migrations.AddField(
            model_name='registro',
            name='mesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.mesa'),
        ),
    ]
