import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/?action=click&contentCollection=undefined&region=TopBar&module=HomePage-Title&pgtype=sectionfront')
soup = BeautifulSoup(r.content, 'lxml')

nav = soup.nav
for i in nav.find_all('a'):
	print(i.get('href'))

body = soup.body
for i in body.find_all('p'):
	print(i.text)

for i in soup.find_all('div', {'class':'collection headlines'}):
	print(i.text)




r = requests.get('http://spiderbites.nytimes.com/')
soup = BeautifulSoup(r.content, 'xml')

for i in soup.find_all('a'):
	print(i.get('href'))