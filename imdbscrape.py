from datetime import date
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

#appends a given episode to episodes.txt 
#show, episode, and airdate required
def addEpisode(show, episode, airdate):	
	print("adding episode")
	with open('episodes.txt', 'a', encoding='utf-8') as episodes:
		episodes.write(show + ': ') #writes show name
		#writes/locates season and episode # in episode soup obj
		episodes.write(episode.find(
			'div', {'class': 'image'}).find('div').find('div').contents[0] + '\n')
		#writes/locates episode title in episode soup obj
		episodes.write('\t' + episode.find('a').get('title') + '| ')
		#writes airdate 
		episodes.write(airdate[0] + ' ' +  airdate[1] + ' ' +  airdate[2])
		episodes.write('\n')

#finds new episodes of a tv show on imdb with a given link
def findNewEpisodes(link, time):
	new = True

	#reads html from given link
	client = uReq(link)
	html = client.read()
	client.close()

	#parses html into soup obj
	page = soup(html, 'html.parser')

	#finds show name
	show = page.find('h1').contents[0].strip()
	print("Finding new episodes for: ", show)

	#locates season links in tv show home page
	seasonLinks = page.find('div', {'class': 'seasons-and-year-nav'})
	for link in seasonLinks.find_all('a'): #loops through all the links
		season = 'https://www.imdb.com' + link.get('href')
		#executes if the link is to a season and the episodes are still new
		if('season' in season and new):
			#reads html from link to season
			client = uReq(season)
			html = client.read()
			client.close()
	
			#parses html into soup obj
			page = soup(html, 'html.parser')

			#locates list of episodes in the html
			episodes = page.find('div', {'class': 'list detail eplist'})
			#loops through all episode list items starting from the newest
			for episode in reversed(episodes.find_all('div', {'class': 'list_item'})):
				#locates airdate of episode 
				airdate = episode.find('div', {'class': 'airdate'}).contents[0].split()
				#checks if episode is considered new and if so adds episode to text file
				#otherwise sets new to False
				if(len(airdate) == 3):
					if(int(airdate[2]) > time.year):
								addEpisode(show, episode, airdate)
					elif(int(airdate[2]) == time.year):
						if(months[airdate[1]] > time.month):	
								addEpisode(show, episode, airdate)
						elif(months[airdate[1]] == time.month):
							if(int(airdate[0]) >= time.day):				
								addEpisode(show, episode, airdate)
							else: new = False
						else: new = False
					else: new = False

#goes through urls in text file and checks for new episodes
def searchShows(time):
	with open('urls.txt') as urls:
		for line in urls:
			findNewEpisodes(line, time)
		
#dictionary used to convert month name to month number
months = {'Jan.': 1, 'Feb.': 2, 'Mar.': 3, 'Apr.': 4,
		'May': 5, 'Jun.': 6, 'Jul.': 7, 'Aug.': 8,
		'Sep.': 9, 'Oct.': 10, 'Nov.': 11, 'Dec.': 12}	

#calls search shows function
#checks for command line argument that specifies date to start from
#arguments should be entered in this order: year, month, day
#if none, default is set as todays date
if(len(sys.argv) == 4):
	searchShows(date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else: searchShows(date.today())
