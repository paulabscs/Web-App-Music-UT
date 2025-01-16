from pydantic import BaseModel
from typing import List

class TrackDTO(BaseModel):
    """
    /* Data Transfer Object representing a track.
       All fields are required as the client doesn't 
       have access to the modifier API (read-only).
    */"""
    track_id: int
    track_title: str
    track_duration: int
    album_title: str
    artist_name: str
    track_image_file: str
