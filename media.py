import webbrowser


class Movie():
    """
    This is a class for Movies

    Attributes:
            title: Movie title
            storyline: A brief description of the movie's storyline
            poster_image_url: A URL of the movie's poster image
            trailer_youtube_url: A URL of the movie's YouTube trailer.

    """

    def __init__(
            self,
            title,
            storyline,
            poster_image_url,
            trailer_youtube_url):
        """
        The constructor for the Movie Class

        Args:
                title (str): Movie title
                storyline (str): A brief description of the movie's storyline
                poster_image_url (str): A URL of the movie's poster image
                trailer_youtube_url (str): A URL of the movie's YouTube trailer.ube_url (str):
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        A function that passes the Movie's trailer_youtube_url to the webbrowser's open
        function - webbrower.open() displays the URL using the default browser.
        """
        webbrowser.open(self.trailer_youtube_url)
