### Python Commandline Tool to Find New Music ###

import urllib2
from bs4 import BeautifulSoup

pitchfork_album_url = 'http://pitchfork.com/reviews/best/albums/'
output = [[0 for i in xrange(5)] for i in xrange(5)]

# Get ingredients
def get_url(url):
	usock = urllib2.urlopen(url)
	data = usock.read()
	usock.close()
	return data

# Make soup
def make_soup(data):
	soup = BeautifulSoup(data).find(id='content').find(class_='object-list bnm-list')
	return soup

# Get artists from soup
def get_artists(soup):
	artist_soup = soup.find_all('h1')

	i = 1
	y = 0
	while  i < len(artist_soup):
		output[y][0] = artist_soup[i].contents[0]
		i += 2
		y += 1

# Get albums from soup
def get_albums(soup):
	album_soup = soup.find_all('h2')

	i = 0
	while i < len(album_soup):
		output[i][1] = album_soup[i].contents[0]
		i += 1

# Get ratings from soup
def get_ratings(soup):
	rating_soup = soup.find_all('span', 'score')

	i = 0
	while i < len(rating_soup):
		output[i][2] = rating_soup[i].contents[0]
		i += 1

# Pretty print results
def pretty_print():
	print("New music from Pitchfork:")
	for i in xrange(0, len(output)):
		print(output[i][0] + ' - ' + output[i][1] + '. Rating: ' + output[i][2])

def main():
	data = get_url(pitchfork_album_url)
	soup = make_soup(data)

	get_artists(soup)
	get_albums(soup)
	get_ratings(soup)
	pretty_print()

if __name__ == "__main__":
	main()


