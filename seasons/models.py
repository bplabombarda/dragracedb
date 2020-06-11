from django.db import models


class Season(models.Model):
    class Meta:
        db_table = 'season'

    name = models.TextField(default='')
    season_number = models.IntegerField(default=0)
    season_type = models.TextField(default='')

    def __str__(self):
        return self.name
