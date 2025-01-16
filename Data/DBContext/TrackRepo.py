import json
from sqlalchemy.orm import Session
from Data.Models.Track import Track

class TrackRepository:
    def __init__(self, session: Session):
        self.session = session

    def populate_database(self, df):
        """
        /* Parses the DataFrame and populates the track database. 
           A required process to sync the JSON data with the database.
        */"""
        tracks = []
        for index, row in df.iterrows():
            tracks.append(Track(
                track_id=row['track_id'],
                track_title=row['track_title'],
                track_duration=row['track_duration'],
                album_title=row['album_title'],
                artist_name=row['artist_name'],
                track_image_file=row['track_image_file']
            ))

        for t in tracks:
            self.session.add(t)
        self.session.commit()

    def get_tracks(self):
        """
        /* Returns all track records from the database.
           Essential for accessing complete track data.
        */"""
        return self.session.query(Track).all()
