class Actor:
    # First actor in list is self in case a request asks for distance to self
    def __init__(self, name, actor, movie):
        self.name = name
        self.actors = [name]
        self.movies = [movie]

