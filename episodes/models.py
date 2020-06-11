from datetime import date

from django.db import models


class Episode(models.Model):
    queens = models.ManyToManyField(
        'queens.Queen',
        through='EpisodeQueen',
    )
    class Meta:
        db_table = 'episode'

    season = models.ForeignKey(
        'seasons.Season',
        on_delete=models.CASCADE
    )
    air_date = models.DateField(default=date.today)
    episode_number = models.IntegerField(null=True)
    main_challenge_desc = models.TextField(default='')
    mini_challenge_desc = models.TextField(default='')

    def episode_long_name(self):
        return f"{self.season.name} Episode {self.episode_number}"

    def season_episode_notation(self):
        return f"S{self.season.season_number:02d}E{self.episode_number:02d}"

    def __str__(self):
        return self.episode_long_name()


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
