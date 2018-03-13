#!/usr/bin/env python

"""Application init module"""


from tmdb import TMDB
from media_manager import MediaManager
import fresh_tomatoes

__author__ = "Christiaan Lombard <base1.christiaan@gmail.com>"


# initialize api and media manager
api = TMDB("e8b472cbe1c343ed368509f11912186f")
manager = MediaManager(api)

# get lists of movies
print "Getting a list of popular movies..."
popular_movies = manager.list_popular_movies()

print "Getting a list of favorite movies..."
favorite_movies = manager.list_favorite_movies()

# create HTML and open in browser
fresh_tomatoes.open_movies_page(favorite_movies, popular_movies)
