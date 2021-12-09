import csv
import requests
from bs4 import BeautifulSoup
import imdb
ia = imdb.IMDb()

url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-11-01&languages=en&view=simple&count=250'

movieIDs = []
output = []

#function for generating the ids on a page
def generateIDs(pageUrl):
    response = requests.get(pageUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_data = soup.findAll('div', attrs={'class': 'lister-item mode-simple'})

    for blocks in page_data:
        movieData = blocks.div.a
        movieID = movieData.get('href')
        #since the codes are different lengths, just take all until the end of href block which goes until /
        movieID = movieID[9:18]
        #remove '/'
        movieID = movieID.replace('/', '')
        movieIDs.append(movieID)


#generates ids for 2000 movies
generateIDs(url)
pageStart = 251
while (pageStart < 20000):
    url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-11-01&languages=en&view=simple&count=250&start=' + str(pageStart) + '&ref_=adv_nxt'
    generateIDs(url)
    pageStart += 250

outputIndex = 0
uniqueActors = set()
error = False
for ID in movieIDs:
    # getting the movie from the respective ID and checking if there is a cast
    movie = ia.get_movie(ID)
    try:
        movie['cast']
        movie['title']
    except KeyError:
        error = True

    # Throws an error if there is no cast and skips adding the cast to the dict
    if error:
        error = False
        continue

    # Adds the cast to the dict as an associated array and a set to track the number of unique actors
    output.append([])
    output[outputIndex].append(movie['title'])
    for actor in movie['cast']:
        output[outputIndex].append(actor['name'])
        uniqueActors.add(actor['name'])
    
    outputIndex += 1

    # Once the number of unique actors exceeds 100,000, stop adding actors
    if len(uniqueActors) >= 100000:
        break

with open('verticesFinal.csv', 'w', newline='') as file:
    sheet = csv.writer(file)
    for row in output:
        sheet.writerow(row)