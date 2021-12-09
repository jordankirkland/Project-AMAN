import csv
from queue import Queue
from collections import defaultdict
from Actor import Actor

class Graph:

    def __init__(self):
        # Map of actor name strings to Actor objects
        lookUp = {}

        # for loop to iterate through each line of the file,

        with open('verticesFinal.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)

            # For each row in the file
            for row in reader:

                # Temp variables for movie
                movie = row[0]

                # For each actor in the row
                for actor in row[1:]:
                    if not actor:
                        break

                    actorLow = actor.lower()
                    # If the actor exists in the graph already, append the movie
                    # and actor to the list and map respectively
                    if actorLow in lookUp:
                        # Appending movie
                        lookUp[actorLow].movies.append(movie)

                        # Iterating through the list of actors again and adding them to the Actor submap, "actors"
                        for vertice in row[1:]:
                            # Don't add actor to own 'actors'
                            if vertice == actor:
                                continue
                            # When adding the actors to the submap, add them in a pair with both the name and movie "edge"
                            lookUp[actorLow].actors[
                                vertice.lower()] = movie  # does this duplicate actor in their own costars
                    else:
                        # Creating an actor
                        lookUp[actorLow] = Actor(actor, movie)

                        # Iterating through the list of actors again and adding them to the Actor submap, "actors"
                        for vertice in row[1:]:
                            # Don't add actor to own 'actors'
                            if vertice == actor:
                                continue
                            # When adding the actors to the submap, add them in a pair with both the name and movie "edge"
                            lookUp[actorLow].actors[vertice.lower()] = movie
        self.lookUp = lookUp

    def BFS(self, startVertex, endVertex):

        try:
            self.lookUp[startVertex]
            self.lookUp[endVertex]
        except KeyError:
            print("Invalid actor name(s). Please try again.")
            return

        if startVertex == endVertex:
            print(self.lookUp[startVertex].name + " and " + self.lookUp[
                endVertex].name + " are 0 movie(s) apart. Below is the movie path and actor path.")
            print([self.lookUp[startVertex].movies[0]])
            print([self.lookUp[startVertex].name])
            return

        # visited vertices
        visited = set()
        visited.add(startVertex)
        # queue of paths to track
        q = Queue()
        path = [self.lookUp[startVertex]]
        q.put(path)

        while q:
            path = q.get()
            vertex = path[-1]
            if vertex == self.lookUp[endVertex]:
                self.BFSHelper(path)
                return
            elif vertex not in visited:
                for adjacentActor in vertex.actors:  # breaks here, thinks vertex is 'str'? but should be an actor
                    newPath = list(path)
                    newPath.append(self.lookUp[adjacentActor])
                    q.put(newPath)

                visited.add(vertex.name)

    def BFSHelper(self, actors):
        moviePath = []
        actorPath = []
        movies = []
        for actor in actors:
            actorPath.append(actor.name)

            for movie in actor.movies:
                if movie in movies:
                    moviePath.append(movie)
            movies = actor.movies


        print(actorPath[0] + " and " + actorPath[-1] + " are " + str(len(actorPath) - 1) + " movie(s) apart. Below is the movie path and actor path.")
        print(moviePath)
        print(actorPath)

    def Dijkstra(self, startVertex, endVertex):
        # Edge case for actor not in the graph
        try:
            self.lookUp[startVertex]
            self.lookUp[endVertex]
        except KeyError:
            print("Invalid actor name(s). Please try again.")
            return

        # Checking if the start and end vertex are the same (edge case)
        if startVertex == endVertex:
            print(self.lookUp[startVertex].name + " and " + self.lookUp[
                endVertex].name + " are 0 movie(s) apart. Below is the movie path and actor path.")
            print([self.lookUp[startVertex].movies[0]])
            print([self.lookUp[startVertex].name])
            return

        # Queue for holding all the unique vertices (Actors)
        q = Queue()

        # Set for making sure the queue only has unique vertices (Actor names, strings)
        visited = set()

        # Map for linking (distance, previous actor, movie connecting) with actor names (strings)
        distances = {}

        # Uninitialized map to make code a little more readable
        neighbors = {}

        # Creating a minimum distance variable to prevent running longer than needed
        currentMinimum = 1000000

        #######   Resizing vector part? ##########
        # When checking distance, check if actor is added. If it is, compare distance
        # else compare to max int?

        # Initializing the queue with the source Actor and the current distance
        q.put(self.lookUp[startVertex])
        currentDistance = 0

        # Initializing the starting vertex distance
        distances[startVertex] = (0, startVertex, 'N/A')

        while not q.empty():
            # Popping the front element, assigning neighbors to the adjacent actors for readability
            current = q.get()
            neighbors = current.actors

            # Adding the current actor to the visited map and updating currentDistance based on the current vertice
            visited.add(current.name.lower())
            currentDistance = distances[current.name.lower()][0]

            # Once a path has been found between the two vertexes, update current minimum to skip excessively long paths
            if endVertex in distances:
                currentMinimum = distances[endVertex][0]

            if currentDistance >= currentMinimum:
                continue

            # Iterate through the keys in neighbors (the costars of the current actor) (costar is a string)
            for costar in neighbors:

                # If the costar is already in the distances map, check to see if the current path is shorter than the saved one
                if costar in distances:
                    if (distances[costar][0] > (currentDistance + 1)):
                        # If it is shorter, update the distance, previous actor, and shared movie
                        distances[costar][0] = (currentDistance + 1)
                        distances[costar][1] = current.name.lower()
                        distances[costar][2] = neighbors[costar]
                else:
                    # If the costar is not already in the map, add it to the map with the appropriate tuple of data
                    distances[costar] = (currentDistance + 1, current.name.lower(), neighbors[costar])

                # Check if the costar is in the set of visited vertices. If not, add to the queue and mark as visited
                if costar not in visited:
                    q.put(self.lookUp[costar])
                    visited.add(costar)

        # Creating a list of the movie path and actor path between the two actors
        actorPath = [self.lookUp[endVertex].name]
        moviePath = [distances[endVertex][2]]
        currentActor = distances[endVertex][1]
        while currentActor != startVertex:
            # Adding the actor to the path
            actorPath[:0] = [self.lookUp[currentActor].name]

            # Adding the movie to the path
            moviePath[:0] = [distances[currentActor][2]]

            # Updating current actor to the previous actor vertice determined by Dijkstra's above
            currentActor = distances[currentActor][1]

        # Adding the starting actor to the beginning of the path
        actorPath[:0] = [self.lookUp[startVertex].name]

        # Printing out the data
        print(self.lookUp[startVertex].name + " and " + self.lookUp[endVertex].name + " are " + str(
            distances[endVertex][0]) + " movie(s) apart. Below is the movie path and actor path.")
        print(moviePath)
        print(actorPath)

        return
