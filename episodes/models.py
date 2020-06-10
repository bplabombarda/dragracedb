from datetime import date

from django.db import models


class Episode(models.Model):
    class Meta:
        db_table = 'episode'

    season = models.ForeignKey(
        'seasons.Season',
        on_delete=models.CASCADE
    )
    air_date = models.DateField(default=date.today)
    main_challenge_desc = models.TextField(default='')
    mini_challenge_desc = models.TextField(default='')
    episode_number = models.IntegerField(null=True)


class EpisodeQueen(models.Model):
    class Meta:
        db_table = 'episode_queen'

    episode = models.ForeignKey(
        Episode,
        on_delete=models.CASCADE
    )
    queen = models.ForeignKey(
        'queens.Queen',
        on_delete=models.CASCADE
    )
    main_challenge_result = models.TextField(default='')
    mini_challenge_result = models.TextField(default='')
