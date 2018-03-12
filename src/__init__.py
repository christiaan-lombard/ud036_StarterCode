
from tmdb import TMDB
from media_manager import MediaManager
import fresh_tomatoes

api = TMDB("e8b472cbe1c343ed368509f11912186f")
manager = MediaManager()

popular_movies = api.list_popular_movies()
favorite_movies = manager.list_favourite_movies()

fresh_tomatoes.open_movies_page(favorite_movies, popular_movies)
