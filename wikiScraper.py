import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text


soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})


links = My_table.find_all('a')
#print(links)

countries = []

for link in links:
	countries.append(link.get('title'))
	
print(countries)