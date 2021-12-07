import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&view=simple&count=250'
#'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&start=51&ref_=adv_nxt'
#'https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1950-01-01,2021-12-31&languages=en&start=101&ref_=adv_nxt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

link = []

page_data = soup.findAll('div', attrs={'class': 'lister-item mode-simple'})

for blocks in page_data:
    link = blocks.div.a.text

print(link)