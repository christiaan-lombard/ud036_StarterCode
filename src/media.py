

class Video():
    def __init__(self, title, overview, poster_image_url):
        self.title = title
        self.overview = overview
        self.poster_image_url = poster_image_url


class Movie(Video):
    def __init__(self, title, overview, poster_image_url, release_date, trailer_youtube_url):
        Video.__init__(self, title, overview, poster_image_url)
        self.release_date = release_date
        self.trailer_youtube_url = trailer_youtube_url
