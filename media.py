# movie class blueprint

import webbrowser


class Movie():

    """ This class provides information about the movie.

    Attributes:
        title storyline poster_image_url trailer_youtube_url release_date
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):

        # initialises variables with respective values

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    def show_trailer(self):

        # Plays the movie trailer in the web browser.

        webbrowser.open(self.trailer_youtube_url)
