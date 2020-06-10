from utils.loader import DragRaceLoader


def run():
    loader = DragRaceLoader()
    loader.truncate_tables()
    loader.process_data()
    loader.load_data()
