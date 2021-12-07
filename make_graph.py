import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)








#Imdbpy stuff I'm ignoring for now

# from imdb import IMDb 
# ia = IMDb()


# # Function get_movies() using beautiful soup and the url to scrape 
# # movie names from our search and store them in a .txt file


# # Read in each movie and use imdbpy to access the actor lists?
# matrix = ia.get_movie('0133093')
# matrix.infoset2keys
# for item in matrix['cast']:
#     print(item)
