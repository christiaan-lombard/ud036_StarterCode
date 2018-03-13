
import urllib
import json
from media import Movie


class TMDB():
    """A wrapper for The Movie Database API

    See: https://www.themoviedb.org/documentation/api

    Attributes:
        base_url -- The base url for making api requests
        image_url -- The base url for getting images

    """

    base_url = "https://api.themoviedb.org/3"
    image_url = "http://image.tmdb.org/t/p/w300"

    def __init__(self, api_key):
        """Create a new TMDB instance

        Arguments:
            api_key {string} -- The api key issued by TMDB to authorize
                                API requests
        """

        self.api_key = api_key

    def get_movie_details(self, id):
        """Get the detailed information of a movie

        Arguments:
            id {integer} -- The TMDB movie id

        Returns:
            dict -- The detailed information about the movie
        """

        return self._request(
            "movie/" + str(id),
            {
                'append_to_response': 'videos',
                'language': 'en-US'
            })

    def list_popular_movies(self):
        """Get a list of popular movies

        Returns:
            list -- The list of popular movies
        """

        return self._request(
            "movie/popular",
            {
                'language': 'en-US',
                'page': 1
            })

    def _request(self, slug, params):
        """Sends an API request

        Arguments:
            slug {string} -- Part of the url to be appended to the base_url
            params {dict} -- Parameters added to the request as a query string

        Returns:
            dict -- The JSON decoded response
        """

        params['api_key'] = self.api_key
        url = self.base_url + "/" + slug + "?" + urllib.urlencode(params)
        conn = urllib.urlopen(url)
        response = conn.read()
        # print response
        conn.close()
        return json.loads(response)
