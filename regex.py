from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


def getdata(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		soup = BeautifulSoup(html, 'lxml')
		data = soup.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/.*\.jpg")})
	except AttributeError as e:
		return None
	return(data)

data = getdata('http://www.pythonscraping.com/pages/page3.html')

if data is None:
	print('data could not be found')
else:
	for i in data:
		print(i["src"])
