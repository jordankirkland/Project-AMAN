import pandas as pd
import requests
from bs4 import BeautifulSoup
import imdb
#import omdb
ia = imdb.IMDb()

url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250'
# 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250&start=251&ref_=adv_nxt'
# 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250&start=501&ref_=adv_nxt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

movieIDs = []
movies = []
actors = []


page_data = soup.findAll('div', attrs={'class': 'lister-item mode-simple'})

for blocks in page_data:
    movieData = blocks.div.a
    movieID = movieData.get('href')
    #since the codes are different lengths, just take all until the end of href block which goes until /
    movieID = movieID[9:18]
    #remove '/'
    movieID = movieID.replace('/', '')
    movieIDs.append(movieID)


i = 1
for ID in movieIDs:
    movie = ia.get_movie(ID)
    for actor in movie['cast']:
        actors.append(actor)
        movies.append(movie)    
        print(i)
        i += 1

# Should make a basic column sheet, still need to think about how to handle duplicate actors though, maybe through 
# 2d array of movies? Though that may require a map to reaccess the actor with relatively fast time.
sheet = pd.DataFrame({'Actor': actors, 'Movies Featured': movies})

sheet.to_csv('vertices.csv', index = False)
#Will is practicing commit