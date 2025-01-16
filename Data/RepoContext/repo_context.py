from Data.DBContext.context_manager import session_scope
from Data.DBContext.TrackRepo import TrackRepository
from Data.Dtos.track_dto import TrackDTO
from Data.Dtos.track_orm import TrackORM
from Models.Track import Track as NonEntityTrack
from Data.RepoContext.irepo_context import IRepoContext

class RepoContext(IRepoContext):
    def __init__(self, repo_factory):
        """
        /* Initializes the RepoContext with a repository factory.
           Enables the generation of repositories with the given session.
        */
        """
        self.repo_factory = repo_factory

    def get_repo(self):
        """
        /* Retrieves a repository instance within a session scope.
           Ensures thread-safe access to the database.
        */
        """
        with session_scope() as session:
            return self.repo_factory(session)

    def get_tracks_dto(self):
        """
        /* Converts Track records to DTOs for data transfer.
           Facilitates the transportation of track data without 
           exposing internal database models.
        */
        """
        repo = self.get_repo()
        tracks = repo.get_tracks()
        track_dtos = [TrackDTO(
            track_id=track.track_id,
            track_title=track.track_title,
            track_duration=track.track_duration,
            album_title=track.album_title,
            artist_name=track.artist_name,
            track_image_file=track.track_image_file
        ) for track in tracks]
        return track_dtos

    def get_tracks_dict(self):
        """
        /* Converts Track DTOs to JSON-compatible dictionaries.
           Prepares track data for JSON serialization.
        */
        """
        track_dtos = self.get_tracks_dto()
        tracks_dict = [TrackORM.dto_to_json_dict(track_dto) for track_dto in track_dtos]
        return tracks_dict

    def get_tracks_non_entity(self):
        """
        /* Converts Track records to non-entity Track objects.
           Useful for logic operations that don't require ORM features.
        */
        """
        repo = self.get_repo()
        tracks = repo.get_tracks()
        non_entity_tracks = [NonEntityTrack(
            track_id=track.track_id,
            track_title=track.track_title,
            track_duration=track.track_duration,
            album_title=track.album_title,
            artist_name=track.artist_name,
            track_image_file=track.track_image_file
        ) for track in tracks]
        return non_entity_tracks
