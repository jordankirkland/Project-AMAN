import pandas as pd
import requests
from bs4 import BeautifulSoup
import imdb
#import omdb
ia = imdb.IMDb()

url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie,tv_series,tv_miniseries&release_date=,2021-11-01&plot=marvel&view=simple&count=250'
# 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250&start=251&ref_=adv_nxt'
# 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250&start=501&ref_=adv_nxt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

movieIDs = []
actors = {}

page_data = soup.findAll('div', attrs={'class': 'lister-item mode-simple'})

for blocks in page_data:
    movieData = blocks.div.a
    movieID = movieData.get('href')
    #since the codes are different lengths, just take all until the end of href block which goes until /
    movieID = movieID[9:18]
    #remove '/'
    movieID = movieID.replace('/', '')
    movieIDs.append(movieID)


uniqueActors = set()
error = False
for ID in movieIDs:
    # getting the movie from the respective ID and checking if there is a cast
    movie = ia.get_movie(ID)
    try:
        movie['cast']
    except KeyError:
        error = True

    # Throws an error if there is no cast and skips adding the cast to the dict
    if error:
        error = False
        continue

    # Adds the cast to the dict as an associated array and a set to track the number of unique actors
    actors[movie['title']] = []
    for actor in movie['cast']:
        actors[movie['title']].append(actor['name'])
        uniqueActors.add(actor['name'])

    # Once the number of unique actors exceeds 100,000, stop adding actors
    if len(uniqueActors) >= 100000:
        break

output_data = actors.items()
output_list = list(output_data)

# Should make a basic column sheet, still need to think about how to handle duplicate actors though, maybe through 
# 2d array of movies? Though that may require a map to reaccess the actor with relatively fast time.
sheet = pd.DataFrame(output_list)

sheet.to_csv('vertices.csv', index = False)
#Will is practicing commit