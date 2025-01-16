from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Track(Base):
    __tablename__ = 'tracks'
    """
    /* SQLAlchemy model for the tracks table.
       Includes all necessary fields mapped to database columns.
    */"""
    track_id = Column(Integer, primary_key=True)
    track_title = Column(String)
    track_duration = Column(Integer)
    album_title = Column(String)
    artist_name = Column(String)
    track_image_file = Column(String)

    def __repr__(self):
        """
        /* Provides a string representation of the Track model.
           Useful for ORM object inspection.
        */"""
        return (
            f"Track(track_id={self.track_id}, track_title={self.track_title}, "
            f"track_duration={self.track_duration}, album_title={self.album_title}, "
            f"artist_name={self.artist_name}, track_image_file={self.track_image_file})"
        )
