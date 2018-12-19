# store details of movie to display in website

import fresh_tomatoes
import media


def main():

    # contains info about movie like title, storyline etc.

    harry_potter = media.Movie("Harry Potter",
                               "The story of an orphan boy who lived",
                               "https://upload.wikimedia.org/wikipedia/en/b/b5/Harry-film-logo.png",  # noqa
                               "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                               "12 April 2002")

    transformers = media.Movie("Transformers",
                               "Alien giant robots invade earth",
                               "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # noqa
                               "https://www.youtube.com/watch?v=KrUhwet0ngg",
                               "4 August 2007")

    internship = media.Movie("The Internship",
                             "Two persons went to internship in google",
                             "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=cdnoqCViqUo",
                             "26 July 2013")

    matrix = media.Movie("The Matrix",
                         "The world is a simulation",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "March 31, 1999")

    idiots = media.Movie("3 Idiots",
                         "About 3 students college life.",
                         "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=K0eDlFX9GMc",
                         "25 December 2009")

    casino_royal = media.Movie("Casino Royale",
                               "Best James Bond Movie",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg/330px-Casino_Royale_2_-_UK_cinema_poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=36mnx8dBbGE",
                               "14 November 2006")

    # Store the Movie objects in a list.

    movies = [harry_potter,
              transformers,
              internship,
              matrix,
              idiots,
              casino_royal]

    # Open the movie website in the user's browser, featuring the movies above.

    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
