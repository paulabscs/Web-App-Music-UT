from Data.Models.Track import Track as ORMTrack  
from Data.Dtos.track_dto import TrackDTO
from Models.Track import Track as NonEntityTrack

class TrackORM:
    """
    /* Utility class for converting between TrackDTO and Track models.
       Provides static methods to handle various transformations.
    */"""

    @staticmethod
    def dto_to_non_entity(track_dto: TrackDTO) -> NonEntityTrack:
        """
        /* Converts a Data Transfer Object (TrackDTO) to a Non-Entity Track object.
           This method facilitates the transformation of DTOs for internal logic.
        */"""
        return NonEntityTrack(
            track_id=track_dto.track_id,
            track_title=track_dto.track_title,
            track_duration=track_dto.track_duration,
            album_title=track_dto.album_title,
            artist_name=track_dto.artist_name,
            track_image_file=track_dto.track_image_file,
        )

    @staticmethod
    def non_entity_to_dto(track_non_entity: NonEntityTrack) -> TrackDTO:
        """
        /* Converts a Non-Entity Track object to a Data Transfer Object (TrackDTO).
           Essential for preparing data for transfer between different application layers.
        */"""
        return TrackDTO(
            track_id=track_non_entity.track_id,
            track_title=track_non_entity.track_title,
            track_duration=track_non_entity.track_duration,
            album_title=track_non_entity.album_title,
            artist_name=track_non_entity.artist_name,
            track_image_file=track_non_entity.track_image_file,
        )

    @staticmethod
    def dto_to_json_dict(track_dto: TrackDTO) -> dict:
        """
        /* Converts a Data Transfer Object (TrackDTO) to a JSON-compatible dictionary.
           Helps in formatting DTOs for JSON serialization.
        */"""
        non_entity_track = TrackORM.dto_to_non_entity(track_dto)
        return {
            'track_id': non_entity_track.track_id,
            'track_title': non_entity_track.track_title,
            'track_duration': non_entity_track.track_duration,
            'album_title': non_entity_track.album_title,
            'artist_name': non_entity_track.artist_name,
            'track_image_file': non_entity_track.track_image_file,
        }

    @staticmethod
    def non_entity_to_json_dict(track_non_entity: NonEntityTrack) -> dict:
        """
        /* Converts a Non-Entity Track object to a JSON-compatible dictionary.
           Useful for preparing data for JSON serialization.
        */"""
        return {
            'track_id': track_non_entity.track_id,
            'track_title': track_non_entity.track_title,
            'track_duration': track_non_entity.track_duration,
            'album_title': track_non_entity.album_title,
            'artist_name': track_non_entity.artist_name,
            'track_image_file': track_non_entity.track_image_file,
        }
