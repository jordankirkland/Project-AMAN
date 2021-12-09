import csv
from Actor import Actor
from imdb import IMDb
from queue import PriorityQueue
from queue import Queue
from collections import defaultdict
import heapq as heap

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
                    if actor == '':
                        break
                    # If the actor exists in the graph already, append the movie
                    # and actor to the list and map respectively
                    if actor.lower() in lookUp:
                        # Appending movie
                        lookUp[actor.lower()].movies.append(movie)
                        
                        # Iterating through the list of actors again and adding them to the Actor submap, "actors"
                        for vertice in row[1:]:
                            if actor == '':
                                break
                            # When adding the actors to the submap, add them in a pair with both the name and movie "edge"
                            lookUp[actor.lower()].actors[vertice.lower()] = movie  # does this duplicate actor in their own costars
                    else:
                        # Creating an actor
                        lookUp[actor.lower()] = Actor(actor, movie)
                        
                        # Iterating through the list of actors again and adding them to the Actor submap, "actors"
                        for vertice in row[1:]:
                            if actor == '':
                                break
                            # When adding the actors to the submap, add them in a pair with both the name and movie "edge"
                            lookUp[actor.lower()].actors[vertice.lower()] = movie
        self.lookUp = lookUp

    #pass in the string name of the desired vertex
    def Dijkstra(self, startVertex, endVertex):
        #change the string pass into the matching Actor object
        startActor = self.lookUp[startVertex]
        endActor = self.lookUp[endVertex]

        #make a set to track visited and dictionary for the result paths
        visitedVerts = set()
        pMap = {}
        pq = []

        #this keeps track of the minimum cost to reach verts, the starting node is zero
        vertsCost = defaultdict(lambda: map)
        vertsCost[startActor] = 0

        #represents cost to the vertex from the source vertex using a priority queue
        heap.heappush(pq, (0, startActor))

        while pq:
            #would normally go to shortest cost, but everything is cost of 1, pop this one
            _, vert = heap.heappop(pq)

            #if the popped node is the end node, we want to end here
            if vert is endActor:
                break

            visitedVerts.add(vert)

            #loop through the poped's adj actors (costars)
            for costar in startActor.actors:

                #if they havent been visited and have a lower minimum cost, add to parent map
                if costar in visitedVerts:
                    continue

                updatedCost = vertsCost[startActor] + 1 #adding one since thats all of the weights

                if vertsCost[costar] > updatedCost:
                    pMap[costar] = startActor
                    vertsCost[costar] = updatedCost
                    heap.heappush(pq, (updatedCost, costar))
        return pMap, vertsCost

    def printPathDijkstra(self, pMap, endVertex):

        if pMap[endVertex] == -1:
            print(endVertex)
            return

        self.printPathDijkstra(pMap, pMap[endVertex])
        print(endVertex)




    def BFS(self, startVertex):
        # change the string pass into the matching Actor object
        startActor = self.lookUp[startVertex]

        # make a list to track visited
        visited = [False] * len(self.lookUp)

    # Pass in start and end vertex as lowercase strings

    def Dijkstra2(self, startVertex, endVertex):
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
        distances[startVertex] = (0, startVertex, "N/A")

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
        print(self.lookUp[startVertex].name + " and " + self.lookUp[endVertex].name + " are " + str(distances[endVertex][0]) + " movie(s) apart. Below is the movie path and actor path.")
        print(moviePath)
        print(actorPath)

#Same code, just older implementation
# Map of actor name strings to Actor objects
# lookUp = {}

#for loop to iterate through each line of the file, 

# with open('vertices1.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     # For each row in the file
#     for row in reader:
#
#         # Temp variables for movie
#         movie = row[0]
#
#         # For each actor in the row
#         for actor in row[1:]:
#             if not actor:
#                 break
#             if actor == '':
#                 break
#             # If the actor exists in the graph already, append the movie
#             # and actor to the list and map respectively
#             if actor.lower() in lookUp:
#                 lookUp[actor.lower()].movies.append(movie)
#                 for vertice in row[1:]:
#                     if actor == '':
#                         break
#                     lookUp[actor.lower()].actors[vertice.lower()] = movie #does this duplicate actor in their own costars
#             else:
#                 lookUp[actor.lower()] = Actor(actor, movie)
#                 for vertice in row[1:]:
#                     if actor == '':
#                         break
#                     lookUp[actor.lower()].actors[vertice.lower()] = movie
# print("hi")
# # Read in each movie and use imdbpy to access the actor lists?
# matrix = ia.get_movie('0133093')
# for item in matrix['cast']:
#     print(item)

