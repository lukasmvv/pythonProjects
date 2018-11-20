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
	
# This function takes in a string and determines what RGB colours are to be used for that countries scores
def getTeamRGB(team,n):
	colors = np.zeros((n,4)) # Adding fourth column for opacity which will be changed later when scores are checked
	rgb = []
	if team == "Argentina":
		rgb = [102,178,255]
	elif team == "Australia":
		rgb = [255,255,0]
	elif team == "England":
		rgb = [255,0,0]
	elif team == "France":
		rgb = [0,0,204]
	elif team == "Italy":
		rgb = [255,51,255]
	elif team == "Ireland":
		rgb = [102,255,178]
	elif team == "New Zealand":
		rgb = [0,0,0]
	elif team == "Scotland":
		rgb = [102,255,255]
	elif team == "South Africa":
		rgb = [0,153,0]
	elif team == "Wales":
		rgb = [255,153,153]
	else:
		rgb = [160,160,160]
	
	# Dividing by 255 to get colors in range 0-1
	colors[:,0] = rgb[0]/255
	colors[:,1] = rgb[1]/255
	colors[:,2] = rgb[2]/255
	return colors
	
# This function takes in two strings and returns the string that will lead to a valid Wikipedia page
def defineURL(team1, team2):
	return ('https://en.wikipedia.org/wiki/History_of_rugby_union_matches_between_'+min(team1, team2)+'_and_'+max(team1, team2)).replace(' ','_')

	
	
# Given data and the score index, this function returns the data as ints ordered according to WINNER-LOSER
def orderScores(data,scoreIndex,winnerIndex,num,team1,team2):
	new_scores = []
	scores = getCol(data,scoreIndex)
	#print(scores)
	winners = getCol(data,winnerIndex)
	
	# Finding winner base for ordering 
	winner_base = winners[0]
	i = 1
	while winner_base == "Winner" or winner_base == "Draw":
		i = i + 1
		winner_base = winners[i]
	
	if team1 != winner_base:
		team2 = team1
		team1 = winner_base
	i = 0
	for i in range(num+1):
		if scores[i] != 'Score':
			scores[i] = scores[i].replace(' ','')
			#score = score.replace('–',',')
			new_scores_temp = scores[i].split('–')
			winner_score = max(int(new_scores_temp[0]),int(new_scores_temp[1]))
			loser_score = min(int(new_scores_temp[0]),int(new_scores_temp[1]))
			#print(new_scores[1])
			if data[i][winnerIndex] == "Draw" or data[i][winnerIndex] == "draw":
				new_scores.append([-loser_score, winner_score, 0.4, 0.4])
			elif data[i][winnerIndex] != winner_base:
				new_scores.append([-loser_score, winner_score, 0.1, 1])
			else:
				new_scores.append([-winner_score, loser_score, 1, 0.1])
	return new_scores,team1,team2
		

# Given a Wiki URL, this function reads the results data and returns the ordered scores
def getScores(website_url,team1,team2):

	# Initialising data list
	data = []
	row = 0
	col = 0
	row_counter = 0

	# Setting column index values - this can be made smarter by looping through table and looking for headings
	num_index = 0
	date_index = 1
	venue_index = 2
	score_index = 3
	winner_index = 4
	comp_index = 5
	
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
		if headings[0] == 'No.':
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
		
		if row_counter != 0:
			# Appending empty data to list
			data.append(['','','','','',''])

			# Looping through found headings in row (should only be 1)
			#for th in ths:
			data[row][col] = row
			col = col + 1
			
			# Lopoing through found data entries (should be 5, except when competition is repeated)
			for td in tds:
				if col < 6:
					data[row][col] = td.text.strip()
					col = col + 1
				
			# Checking if competition is empty. If so, reuse previous rows competition. This is because the wikitable has competitions spanning multiple rows. Quick hack which does not work. MUST FIX!
			if data[row][comp_index] == '':
				data[row][comp_index] = data[row-1][comp_index]

			row = row + 1
		row_counter = row_counter + 1
		
	new_scores, team1, team2, = orderScores(data,score_index, winner_index, int(data[row-1][num_index]),team1,team2)
	return new_scores,data,row,num_index, team1, team2, row+1


	
# Imports
import requests
from bs4 import BeautifulSoup
import numpy as np
from matplotlib import pyplot as plt
import math
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


team1 = 'South Africa'
team2 = 'Wales'

# new example: https://en.wikipedia.org/wiki/List_of_New_Zealand_rugby_union_Test_matches

# Getting url data
website_url = requests.get(defineURL(team1,team2)).text

# Extracting data
new_scores, data, row, num_index, team1, team2, max_n = getScores(website_url,team1,team2)

# Getting years as a list
dates = getCol(data,1)
new_dates = []
for date in dates:
	if date != "Date":
		new_dates.append(int(date[-4:]))

color1 = getTeamRGB(team1,max_n)
color2 = getTeamRGB(team2,max_n)

for i in range(max_n-1):
	color1[i,3] = new_scores[i][2]
	color2[i,3] = new_scores[i][3]


fig, ax = plt.subplots()

#score_max = max(abs(max(new_scores[0])),max(abs(new_scores[1])))
score_max = 10*math.ceil((max(abs(min(getCol(new_scores,0))),max(getCol(new_scores,1))))/10)

index = np.arange(1,max_n)
score_index_range = np.arange(-score_max,score_max+5,5)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rects1 = ax.barh(index, getCol(new_scores,0), bar_width, color=color1, error_kw=error_config, zorder=1)
rects2 = ax.barh(index, getCol(new_scores,1), bar_width, color=color2, error_kw=error_config, zorder=2)  



ax.set_xlabel("Score")
ax.set_ylabel("Test Match #")
ax.set_title(team1 + " vs " + team2 + " Scores")
ax.set_xticks(score_index_range)
ax.set_autoscale_on(False)
ax.set_yticks(index)

xlabels = []
for i in score_index_range:
	xlabels.append(str(abs(i)))
ax.set_xticklabels(xlabels)

#team1_label = mpatches.Patch(color=[color1[0][0],color1[0][1],color1[0][2]], label=team1)
#team2_label = mpatches.Patch(color=[color2[0][0],color2[0][1],color2[0][2]], label=team2)
#agg_label = mpatches.Patch(color='red', label='Aggregate')

legend_elements = [Patch(color=[color1[0][0],color1[0][1],color1[0][2]], label=team1),
				   Patch(color=[color2[0][0],color2[0][1],color2[0][2]], label=team2), 
				   Line2D([0], [0], marker='o', color='r', label='Diff',
                          markerfacecolor='r', markersize=10)]
#legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
 #                  Line2D([0], [0], marker='o', color='w', label='Scatter',
  #                        markerfacecolor='g', markersize=15),
   #                Patch(facecolor='orange', edgecolor='r',
    #                     label='Color Patch')]
ax.legend(handles=legend_elements)
#ax.legend(handles=[team1_label, team2_label, agg_label])


score_offset = 1
for i in range(0,max_n-1):
	plt.text(new_scores[i][0]-score_offset, i+1, str(abs(new_scores[i][0])),ha='center', va='center')
	plt.text(new_scores[i][1]+score_offset, i+1, str(new_scores[i][1]),ha='center', va='center')
	
ax2 = ax.twinx()

rects3 = ax2.barh(index, getCol(new_scores,0), bar_width, color=color1, error_kw=error_config,
                label=team1, zorder=3)
				
# Finding and plotting aggregate of scores
aggregate = []
for i in range(max_n-1):
	aggregate.append(new_scores[i][0] + new_scores[i][1])

line1 = ax2.plot(aggregate,index,'ro--', zorder=4)				
ax2.set_yticks(index)
ax2.set_yticklabels(new_dates)
# Move left y-axis and bottim x-axis to centre, passing through (0,0)
#ax.spines['left'].set_position('zero')
#ax2.spines['right'].set_position('zero')

# Eliminate upper and right axes
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')



fig.tight_layout()
plt.show()
