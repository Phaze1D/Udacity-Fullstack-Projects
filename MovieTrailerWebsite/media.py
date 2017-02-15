class Movie():
    """
    Movie Class:
        A class that represents a single movie with basic
        information about the movie
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self._title = title
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url



    @property
    def title(self):
        """ title (string): The name of the movie """
        return self._title

    @property
    def poster_image_url(self):
        """ poster_image_url (string): The url for the movie poster """
        return self._poster_image_url

    @property
    def trailer_youtube_url(self):
        """ trailer_youtube_url (string): The url for the movie trailer """
        return self._trailer_youtube_url
