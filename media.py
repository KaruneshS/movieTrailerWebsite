''' @desc this class hold functions about movies
    @author Karunesh karuneshbsarad@gmail.com '''

class Movie():

	''' @desc Constructor to initiate movie object with required details
		@param String title - title of the movie,
			   String storyline - storyline for the movie,
			   String poster - url for the movie poster image
			   String trailer - url for the movie trailer '''

        def __init__(self, title, storyline, poster, trailer):
                self.title = title
                self.storyline = storyline
                self.poster_image_url = poster
                self.trailer_youtube_url = trailer

    
