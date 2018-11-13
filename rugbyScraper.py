# see https://scipython.com/blog/scraping-a-wikipedia-table-with-beautiful-soup/

# This function takes in a list of lists and returns the 'column' of given index i
def getCol(data, i):
	col = []
	for row in data:
		col.append(row[i])
	return col
	
# This function takes in a list of lists and returns the 'row' of given index i
def getRow(data, i):
	return data[i]

# Imports
import requests
from bs4 import BeautifulSoup

# Initialising data list
data = []
row = 0
col = 0

# Setting column index values
num_index = 0
date_index = 1
venue_index = 2
score_index = 3
winner_index = 4
comp_index = 5

# Getting url data
website_url = requests.get('https://en.wikipedia.org/wiki/History_of_rugby_union_matches_between_New_Zealand_and_South_Africa').text

# Adding data to soup object
soup = BeautifulSoup(website_url,'lxml')

# Finding all wikitables
tables = soup.find_all('table',{'class':'wikitable'})

# Search through the tables for the one with the headings we want.
for table in tables:
	# th will find all table headings
	ths = table.find_all('th')
	headings = []
	
	# Loop through found headings and check if it matches our desired headings
	for th in ths:
		headings.append(th.text.strip())		
	if headings[:6] == ['No.','Date','Venue','Score','Winner','Competition']:
		# We break here so that table remains and we can use it in the following loop
		break
	
# Looping through rows in found table
for tr in table.find_all('tr'):
	# Setting column index to 0
	col = 0
	
	# Finding all data entries in table row
	tds = tr.find_all('td')
	
	# Finding all headings (in this case first col) in row
	ths = tr.find_all('th')
	
	# Appending empty data to list
	data.append(['','','','','',''])
	
	# Looping through found headings in row (should only be 1)
	for th in ths:
		data[row][col] = th.text.strip()
		col = col + 1
	
	# Lopoing through found data entries (should be 5, except when competition is repeated)
	for td in tds:
		data[row][col] = td.text.strip()
		col = col + 1
		
	# Checking if competition is empty. If so, reuse previous rows competition. This is because the wikitable has competitions spanning multiple rows
	if data[row][comp_index] == '':
		data[row][comp_index] = data[row-1][comp_index]

	row = row + 1

print(data)
