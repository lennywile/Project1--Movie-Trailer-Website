###############################################################################
#
# mymovies.py:   Lenny Wile
#                03/01/2015
#       This code instantiates the Movies class, which is defined in media.py.
#       There are 6 different movies, all of which
#       are classics.  After the instances are created, they are added to an
#       array, which is passed to the open_movies_page
#       method that is provided to us and is defined in fresh_tomatoes.py.
#       This function renders the web page with our six
#       movies, adding a link to the movie's trailer.
#
#
###############################################################################

import media  # class definition for Movies
import fresh_tomatoes  # provided to us for displaying web pages

# let's instantiate the Movie class with our favorite movies

animal_house = media.Movie("Animal House",
                           "An educational classic of Greek college living in \
                           the 1960's",
                           "http://upload.wikimedia.org/wikipedia/en/e/ea/ \
                           Animalhouseposter.jpg",
                           "https://www.youtube.com/watch?v=BoS3-yHoaSY")


caddyshack = media.Movie("Caddyshack",
                         "The authoritative golfing movie",
                         "http://upload.wikimedia.org/wikipedia/en/8/8 \
                         4/Caddyshack_poster.jpg",
                         "https://www.youtube.com/watch?v=zrTqenN1SqQ")


stripes = media.Movie("Stripes"
                      "Why everyone should join the US Army",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Stripes \
                      poster.jpg/220px-Stripesposter.jpg",
                      "https://www.youtube.com/watch?v=Md4Xk-PbSpk")


godfather = media.Movie("The GodFather",
                        "New York crime family entertainment at its best",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/1c/God \
                        father_ver1.jpg/220px-Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")


rudy = media.Movie("Rudy",
                   "How to make money by being bad at football",
                   "http://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",
                   "https://www.youtube.com/watch?v=eDKOlH0I0nQ")


hoosiers = media.Movie("Hoosiers",
                       "An early version of the Spurs",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/8/8d/ \
                       Hoosiers_movie_poster_copyright_fairuse.jpg/220px- \
                       Hoosiers_movie_poster_copyright_fairuse.jpg",
                       "https://www.youtube.com/watch?v=33DEm0eW-wU")

# now add the instances to an array of instances called movies
movies = [animal_house, caddyshack, stripes, godfather, rudy, hoosiers]

# call the method to build the web page
fresh_tomatoes.open_movies_page(movies)
