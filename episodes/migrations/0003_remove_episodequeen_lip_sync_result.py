# Generated by Django 3.0.7 on 2020-06-08 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_auto_20200608_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episodequeen',
            name='lip_sync_result',
        ),
    ]
