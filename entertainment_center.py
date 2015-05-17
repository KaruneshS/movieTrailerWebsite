import media
import fresh_tomatoes

# Movie 1 details "Kal ho na ho"
# @required media.py
khnh = media.Movie("Kal Ho Na Ho",
                   "A story about a person suffering from cancer",
                   "http://upload.wikimedia.org/wikipedia/en/b/b4/KalHoNaaHo.jpg",
                   "https://www.youtube.com/watch?v=tVMAQAsjsOU"
                   )

# Movie 2 details "Rehna na hai tere dilme"
# @required media.py
rhtdm = media.Movie("RHTDM",
                   "A love story",
                   "http://upload.wikimedia.org/wikipedia/en/b/b3/RHTDM.jpg",
                   "https://www.youtube.com/watch?v=FWHb9_C3RTw"
                   )

movies = [khnh, rhtdm]    # List of movies to display in the portal

fresh_tomatoes.open_movies_page(movies)    # Show portal page by passing movies list as a param, @required fresh_tomatoes.py
