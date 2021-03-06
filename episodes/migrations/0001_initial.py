# Generated by Django 3.0.7 on 2020-06-08 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('queens', '0001_initial'),
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_date', models.DateField(default=datetime.date.today)),
                ('lip_sync_artist', models.TextField(default='')),
                ('lip_sync_song', models.TextField(default='')),
                ('main_challenge_desc', models.TextField(default='')),
                ('mini_challenge_desc', models.TextField(default='')),
                ('week_number', models.IntegerField(null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seasons.Season')),
            ],
            options={
                'db_table': 'episodes',
            },
        ),
        migrations.CreateModel(
            name='EpisodeQueen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lip_sync_result', models.TextField(default='')),
                ('main_challenge_result', models.TextField(default='')),
                ('mini_challenge_result', models.TextField(default='')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='episodes.Episode')),
                ('queen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queens.Queen')),
            ],
            options={
                'db_table': 'episode_queens',
            },
        ),
    ]
