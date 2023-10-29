# Generated by Django 3.2.16 on 2023-10-29 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_barrio_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='testigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registro',
            name='numero_de_votos',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]