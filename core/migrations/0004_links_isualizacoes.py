# Generated by Django 5.0.1 on 2024-02-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_links_visualizacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='isualizacoes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]