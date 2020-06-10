from django.db import models


class Season(models.Model):
    class Meta:
        db_table = 'season'

    name = models.TextField(default='')
    season_type = models.TextField(default='')
