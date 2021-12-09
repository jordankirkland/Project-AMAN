import csv
from Actor import Actor
from imdb import IMDb
from queue import PriorityQueue
from collections import defaultdict
import heapq as heap

class Graph:

    def __init__(self):
        # Map of actor name strings to Actor objects
        lookUp = {}

        # for loop to iterate through each line of the file,

        with open('verticesFinal.csv', 'r') as file:
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
                        lookUp[actor.lower()].movies.append(movie)
                        for vertice in row[1:]:
                            if actor == '':
                                break
                            lookUp[actor.lower()].actors[
                                vertice.lower()] = movie  # does this duplicate actor in their own costars
                    else:
                        lookUp[actor.lower()] = Actor(actor, movie)
                        for vertice in row[1:]:
                            if actor == '':
                                break
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
        return pMap

    def printPathDijkstra(self, pMap, endVertex):

        if pMap[endVertex] == -1:
            print(endVertex)
            return

        self.printPathDijkstra(pMap, pMap[endVertex])
        print(endVertex)


    def BFS(self, startVertex, endVertex):
        # change the string pass into the matching Actor object
        startActor = self.lookUp[startVertex.lower()]
        endActor = self.lookUp[endVertex.lower()]

        q = [[startActor]]
        visited = set()

        while q:
            path = q.pop(0)
            vertex = path[-1]
            if vertex == endActor:
                return path
            elif vertex not in visited:
                for adjacentActor in vertex.actors: #breaks here, thinks vertex is 'str'? but should be an actor
                    newPath = list(path)
                    newPath.append(adjacentActor)
                    q.append(adjacentActor)




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

