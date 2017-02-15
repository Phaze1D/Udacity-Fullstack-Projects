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
    with open('movies.json') as data_file:
        data = json.load(data_file)
        for movie in data['movies']:
            rarray.append( Movie(movie['title'], movie['poster_image_url'], movie['trailer_youtube_url']) )

    return rarray


fresh_tomatoes.open_movies_page( movies() )
