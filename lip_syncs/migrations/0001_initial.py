# Generated by Django 3.0.7 on 2020-06-08 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('queens', '0001_initial'),
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LipSync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.TextField(default='')),
                ('artist', models.TextField(default='')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='episodes.Episode')),
            ],
            options={
                'db_table': 'lip_syncs',
            },
        ),
        migrations.CreateModel(
            name='LipSyncQueen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lip_sync', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lip_syncs.LipSync')),
                ('queen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queens.Queen')),
            ],
            options={
                'db_table': 'lip_sync_queens',
            },
        ),
    ]
