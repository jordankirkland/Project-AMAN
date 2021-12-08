import csv
from Actor import Actor
from imdb import IMDb 

# Map of actor name strings to Actor objects
graph = {}

#for loop to iterate through each line of the file, 
currentRow = []

with open('vertices.csv', 'r') as file:
    reader = csv.reader(file)
    
    # For each row in the file
    for row in reader:

        # Temp variables for movie
        currentRow = row
        movie = row[0]

        # For each actor in the row
        for actor in row[1:]:
            if actor == '':
                break
            # If the actor exists in the graph already, append the movie
            # and actor to the list and map respectively
            if actor.lower() in graph:
                graph[actor.lower()].movies.append(movie)
                for vertice in row[1:]:
                    if actor == '':
                        break
                    graph[actor.lower()].actors[vertice.lower()] = movie
            else:
                graph[actor.lower()] = Actor(actor, movie)
                for vertice in row[1:]:
                    if actor == '':
                        break
                    graph[actor.lower()].actors[vertice.lower()] = movie
print("hi")
# # Read in each movie and use imdbpy to access the actor lists?
# matrix = ia.get_movie('0133093')
# for item in matrix['cast']:
#     print(item)
