from django.db import models

from lip_syncs.models import LipSync


class Queen(models.Model):
    episodes = models.ManyToManyField(
        'episodes.Episode',
        through='episodes.EpisodeQueen',
    )
    lip_syncs = models.ManyToManyField(LipSync)


    class Meta:
        db_table = 'queen'

    name = models.TextField(default='', unique=True)
    home_city = models.TextField(default='')
    home_state = models.TextField(default='')
    home_country = models.TextField(default='')

    def __str__(self):
        return self.name
