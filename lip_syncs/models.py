from django.db import models


class LipSync(models.Model):
    class Meta:
        db_table = 'lip_sync'

    episode = models.ForeignKey(
        'episodes.Episode',
        on_delete=models.CASCADE
    )
    song = models.TextField(default='')
    artist = models.TextField(default='')

    def song_artist_notation(self):
        return f"{self.song} by {self.artist}"

    def __str__(self):
        return f"{self.episode.__str__()} {self.song} - {self.artist}"


class LipSyncQueen(models.Model):
    class Meta:
        db_table = 'lip_sync_queen'

    lip_sync = models.ForeignKey(
        LipSync,
        on_delete=models.CASCADE
    )
    queen = models.ForeignKey(
        'queens.Queen',
        on_delete=models.CASCADE
    )
    result = models.TextField(default='')
