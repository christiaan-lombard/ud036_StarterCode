

class Video():
    """A model containing generic video information"""

    def __init__(self, id, title, overview, poster_image_url):
        """Create a Video instance

        Arguments:
            id {string} -- A unique id
            title {[type]} -- Official title
            overview {[type]} -- A introduction of the plot
            poster_image_url {[type]} -- Url to an image
        """

        self.id = id
        self.title = title
        self.overview = overview
        self.poster_image_url = poster_image_url


class Movie(Video):
    """A model containing movie information"""

    def __init__(self, id, title, overview,
                 poster_image_url, release_date, trailer_youtube_url):
        """Create a Movie instance

        Arguments:
            id {string} -- A unique id
            title {[type]} -- The movie's official title
            overview {[type]} -- A introduction of the plot
            poster_image_url {[type]} -- Url to an image
            release_date {[type]} -- YYYY-MM-DD release date
            trailer_youtube_url {[type]} -- Url to youtube trailer
        """

        Video.__init__(self, id, title, overview, poster_image_url)
        self.release_date = release_date
        self.trailer_youtube_url = trailer_youtube_url
