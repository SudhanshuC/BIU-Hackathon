#!/usr/bin/python
import sys
import urllib2
from bs4 import BeautifulSoup
url="http://socialmention.com/search?t=all&btnG=Search&q="
term=sys.argv[1]
comurl=url+term
response=urllib2.urlopen(comurl)
soup = BeautifulSoup(response.read(), "lxml")
print soup.title
print soup.title.string
