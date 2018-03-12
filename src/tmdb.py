
import urllib
import json
from media import Movie

class TMDB():

    base_url = "https://api.themoviedb.org/3"
    image_url = "http://image.tmdb.org/t/p/w300"

    def __init__(self, api_key):
        self.api_key = api_key
    
    def list_popular_movies(self):
        response = self._request("movie/popular", {})
        return self._convert_movie_response(response)

    def _convert_movie_response(self, response):
        results = response['results']
        movies = []
        for result in results:
            movies.append(
                Movie(
                    result['title'], 
                    result['overview'], 
                    self.image_url + result['poster_path'],
                    result['release_date'], 
                    None
                )
            )
        return movies


    def _request(self, slug, params):
        params['api_key'] = self.api_key
        url = self.base_url + "/" + slug + "?" + urllib.urlencode(params)
        # print(url)
        conn = urllib.urlopen(url)
        result = json.load(conn)
        conn.close()
        return result