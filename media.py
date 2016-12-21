import webbrowser
class Movie():
        """This class offers a way to store movie info and
        access related methods.

        Attributes:
        title (str): The title of the movie.
        year (str): Year the movie was released. 
        storyline (str): The plot of the movie.
        poster_img (str): URL to an image of the poster.
        trailer (str): URL to a youtube trailer of the movie.

        Method:
        show_trailer: opens the instance's trailer URL in a browser
        """
	def __init__(self,title,year,storyline,poster_img,trailer):
		self.title = title
		self.year = year
		self.storyline = storyline
		self.poster_image_url = poster_img
		self.trailer_youtube_url = trailer

	def show_trailer(self):
               webbrowser.open(self.trailer_url)

