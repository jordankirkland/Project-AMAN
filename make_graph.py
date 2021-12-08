import pandas as pd
from imdb import IMDb 

pd.read_csv("marvel.csv")

graph = {}

#for loop to iterate through each line of the file



# Read in each movie and use imdbpy to access the actor lists?
matrix = ia.get_movie('0133093')
for item in matrix['cast']:
    print(item)
