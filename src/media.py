

class Video():
    """A model containing generic video information
    
    Attributes:
        id (string): A unique id
        title (string): Official title
        overview (string): A introduction of the plot
        poster_image_url (string): Url to an image
    """

    def __init__(self, id, title, overview, poster_image_url):
        """Create a Video instance"""

        self.id = id
        self.title = title
        self.overview = overview
        self.poster_image_url = poster_image_url


class Movie(Video):
    """A model containing movie information
    
    Attributes:
        id (string): A unique id
        title (string): The movie's official title
        overview (string): A introduction of the plot
        poster_image_url (string): Url to an image
        release_date (string): YYYY-MM-DD release date
        trailer_youtube_url (string): Url to youtube trailer
    """

    def __init__(self, id, title, overview,
                 poster_image_url, release_date, trailer_youtube_url):
        """Create a Movie instance"""

        Video.__init__(self, id, title, overview, poster_image_url)
        self.release_date = release_date
        self.trailer_youtube_url = trailer_youtube_url
