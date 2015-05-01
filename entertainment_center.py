import media
import fresh_tomatoes

khnh = media.Movie("Kal Ho Na Ho",
                   "A story about a person suffering from cancer",
                   "http://upload.wikimedia.org/wikipedia/en/b/b4/KalHoNaaHo.jpg",
                   "https://www.youtube.com/watch?v=tVMAQAsjsOU"
                   )

rhtdm = media.Movie("RHTDM",
                   "A love story",
                   "http://upload.wikimedia.org/wikipedia/en/b/b3/RHTDM.jpg",
                   "https://www.youtube.com/watch?v=FWHb9_C3RTw"
                   )

movies = [khnh, rhtdm]

fresh_tomatoes.open_movies_page(movies)
