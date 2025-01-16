import json
import pandas as pd
from sqlalchemy import create_engine, inspect
from Data.Models.Track import Base
from Data.DBContext.TrackRepo import TrackRepository
from Data.Dtos import track_dto
from Models.Track import Track as NonEntityTrack
from Data.DBContext.context_manager import session_scope

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def setup_database():
    with session_scope() as session:
        inspector = inspect(session.bind)
        track_columns = [col['name'] for col in inspector.get_columns('tracks')]

        if 'track_id' in track_columns:
            track_data = load_json("Data/Source/tracks.json")
            track_df = pd.DataFrame(track_data)
            track_repo = TrackRepository(session)
            track_repo.populate_database(track_df)
        else:
            print("The 'tracks' table does not have a column named 'track_id'.")
            print("Current columns in 'tracks' table:", track_columns)
            Base.metadata.drop_all(session.bind, tables=[Base.metadata.tables['tracks']])
            Base.metadata.create_all(session.bind)
