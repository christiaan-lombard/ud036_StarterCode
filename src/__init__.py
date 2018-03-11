
from tmdb import TMDB
import fresh_tomatoes

api = TMDB("e8b472cbe1c343ed368509f11912186f")
movies = api.popular_movies()

fresh_tomatoes.open_movies_page(movies)