import csv
import os
from datetime import datetime
from io import StringIO

from episodes.models import Episode, EpisodeQueen
from lip_syncs.models import LipSync, LipSyncQueen
from queens.models import Queen
from seasons.models import Season


class DragRaceLoader:
    """Load Drag Race data into Postgres."""

    def __init__(self):
        self.episodes = {}
        self.episode_queens = {}
        self.lip_syncs = {}
        self.lip_sync_queens = {}
        self.queens = {}
        self.seasons = {}

        self.source_data = self.read_file(os.path.abspath("./data/drag_race.csv"))

    def load_data(self):
        Queen.objects.bulk_create(self.queens.values())
        Season.objects.bulk_create(self.seasons.values())
        Episode.objects.bulk_create(self.episodes.values())
        EpisodeQueen.objects.bulk_create(self.episode_queens.values())
        LipSync.objects.bulk_create(self.lip_syncs.values())
        LipSyncQueen.objects.bulk_create(self.lip_sync_queens.values())

    def process_data(self):
        for row in self.source_data:
            queen_name = row.get("queen_name")

            if queen_name not in self.queens:
                self.queens[queen_name] = Queen(
                    id=len(self.queens) + 1,
                    name=queen_name,
                    home_city=row.get("home_city"),
                    home_state=row.get("home_state"),
                    home_country=row.get("home_country"),
                )

            season_name = row.get("season_name")

            if season_name not in self.seasons:

                self.seasons[season_name] = Season(
                    id=len(self.seasons) + 1,
                    name=season_name,
                    season_type=row.get("season_type"),
                )

            week_number = row.get("week_number")
            episode_key = f"{season_name}_{week_number}"

            if episode_key not in self.episodes:
                season = self.seasons.get(season_name)
                date_str = row.get("air_date")
                date_obj = datetime.strptime(date_str, "%m/%d/%Y").date()

                self.episodes[episode_key] = Episode(
                    id=len(self.episodes) + 1,
                    season_id=season.id,
                    air_date=date_obj,
                    main_challenge_desc=row.get("main_challenge_desc", ""),
                    mini_challenge_desc=row.get("mini_challenge_desc", ""),
                    week_number=int(week_number),
                )

            queen = self.queens.get(queen_name)
            episode_queen_key = f"{episode_key}_{queen_name}"
            episode = self.episodes.get(episode_key)

            if episode_queen_key not in self.episode_queens:
                self.episode_queens[episode_queen_key] = EpisodeQueen(
                    id=len(self.episode_queens) + 1,
                    episode_id=episode.pk,
                    queen_id=queen.pk,
                    main_challenge_result=row.get("main_challenge_result", ""),
                    mini_challenge_result=row.get("mini_challenge_result", ""),
                )

            lip_sync_artist = row.get("lip_sync_artist")
            lip_sync_song = row.get("lip_sync_song")
            has_song = bool(lip_sync_artist and lip_sync_song)
            song_key = f"{lip_sync_artist}_{lip_sync_song}"
            lip_sync_key = f"{episode_key}_{song_key}"

            if has_song and lip_sync_key not in self.lip_syncs:
                self.lip_syncs[lip_sync_key] = LipSync(
                    id=len(self.lip_syncs) + 1,
                    episode_id=episode.pk,
                    artist=lip_sync_artist,
                    song=lip_sync_song,
                )

            lip_sync = self.lip_syncs.get(lip_sync_key)
            lip_sync_queen_key = f"{lip_sync_key}_{queen_name}"

            if has_song and lip_sync_queen_key not in self.lip_sync_queens:
                self.lip_sync_queens[lip_sync_queen_key] = LipSyncQueen(
                    id=len(self.lip_sync_queens) + 1,
                    lip_sync_id=lip_sync.pk,
                    queen_id=queen.pk,
                    result=row.get("lip_sync_result", ""),
                )

    def truncate_tables(self):
        Queen.objects.all().delete()
        Season.objects.all().delete()
        Episode.objects.all().delete()
        EpisodeQueen.objects.all().delete()
        LipSync.objects.all().delete()
        LipSyncQueen.objects.all().delete()

    @staticmethod
    def read_file(file_path):
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)

            return list(reader)
