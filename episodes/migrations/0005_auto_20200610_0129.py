# Generated by Django 3.0.7 on 2020-06-10 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0004_auto_20200608_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='week_number',
            new_name='episode_number',
        ),
    ]
