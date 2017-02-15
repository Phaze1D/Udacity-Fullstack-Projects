import json
import fresh_tomatoes
from media import Movie



def movies():
    """
        Functions that reads from a json file called 'movies.json' and
        returns an array of Movies Object

        Returns:
            list (Movie): List of Movie Objects
    """

    rarray = []
    with open('movies.json') as data_file: # opens movies.json file
        data = json.load(data_file) # parse json data
        for movie in data['movies']: # Loop through json array of movies
            rarray.append( Movie(movie['title'], movie['poster_image_url'], movie['trailer_youtube_url']) )

    return rarray


# Opens the static html page on the default browser
fresh_tomatoes.open_movies_page( movies() )
