# Generated by Django 3.0.7 on 2020-06-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('season_type', models.TextField(default='')),
            ],
            options={
                'db_table': 'seasons',
            },
        ),
    ]
