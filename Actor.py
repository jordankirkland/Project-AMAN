class Actor:
    # First actor in list is self in case a request asks for distance to self
    def __init__(self, name, movie):
        self.name = name
        
        # Map of actors costarring with. Key is the costar's name and value is a shared movie, both strings
        self.actors = {}

        # List of movies 
        self.movies = [movie]

