import csv
from imdb import IMDb 

# Map of actor name strings to Actor objects
graph = {}

#for loop to iterate through each line of the file, 
currentRow = []

with open('vertices.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        currentRow = row

# Read in each movie and use imdbpy to access the actor lists?
matrix = ia.get_movie('0133093')
for item in matrix['cast']:
    print(item)
