
##############################################################################
#
#       media.py:       Lenny Wile
#                       03/01/2015
#       Ths code defines the Movie class that is used by mymovies.py (where
#       this class is instantiated).
#       The class has the following properties:
#
#       title - the title of the movie
#       storyline - a brief description of the movie's theme
#       poster_image_url - a link to the movie's poster
#       trailer_youtube_url - a link to the movie's trailer
#
#       The class has the following function:
#
#       open - a function of hte webbrowser standard class, this will open the
#              trailer, given a link to the trailer, and play the trailer when
#              the poster is clicked on the webpage display
#
###############################################################################
import webbrowser  # needed to play the trailer


class Movie():
    """ This class provides a way to strore movie related information"""

    # Movie Properties

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Movie Methods

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
