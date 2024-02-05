# Generated by Django 5.0.1 on 2024-02-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_links_avatar_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='avatar_name',
        ),
        migrations.AddField(
            model_name='links',
            name='link_avatar',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]