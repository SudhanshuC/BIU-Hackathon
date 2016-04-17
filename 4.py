#!/usr/bin/python
import sys
import urllib2
from bs4 import BeautifulSoup
url="http://socialmention.com/search?t=all&btnG=Search&q="
term=sys.argv[1]
comurl=url+term
response=urllib2.urlopen(comurl)
soup = BeautifulSoup(response.read(), "lxml")
allh3=soup.find_all('h3')
for h3 in allh3:
  print "\n\nHere come H3\n\n"
  print h3
