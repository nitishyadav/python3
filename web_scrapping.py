#Web Scrapping
#required to scrap data from TMDB top 250 movies page, having fields movie name , year and rating

from bs4 import BeautifulSoup

import requests
import sys

url = 'http://www.imdb.com/chart/top (http://www.imdb.com/chart/top)'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html5lib')
tr = soup.findChildren('tr')
tr = iter(tr)
#next(tr)

for movie in tr:
    title = movie.find('td',{'class':'titleColumn'}).find('a').contents[0]
    year = movie.find('td',{'class':'titleColumn'}).find('span',{'class':'secondaryInfo'}).contents[0]
    rating =movie.find('td',{'class':'ratingColumn imdbRating'}).find('strong').contents[0]
    row = title+ '-' + year + ''+''+rating
    print(row)
    