class Track:
    def __init__(self, track_id, track_title, track_duration, track_image_file, album_title, artist_name):
        """
        /* Initializes a Track object with essential attributes.
           Necessary for instance representation and manipulation.
        */"""
        self.track_id = track_id
        self.track_title = track_title
        self.track_duration = track_duration
        self.track_image_file = track_image_file
        self.album_title = album_title
        self.artist_name = artist_name

    def __repr__(self):
        """
        /* Provides a string representation of the Track object.
           Useful for debugging and display purposes.
        */"""
        return (f"Track(track_id={self.track_id}, track_title={self.track_title}, "
                f"track_duration={self.track_duration}, track_image_file={self.track_image_file}, "
                f"album_title={self.album_title}, artist_name={self.artist_name})")
