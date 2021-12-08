from imdb import IMDb 
ia = IMDb()


# Function get_movies() using beautiful soup and the url to scrape 
# movie names from our search and store them in a .txt file


# Read in each movie and use imdbpy to access the actor lists?
matrix = ia.get_movie('0133093')
for item in matrix['cast']:
    print(item)


