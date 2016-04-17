#!/usr/bin/python
import sys
import urllib2
url="http://socialmention.com/search?t=all&btnG=Search&q="
term=sys.argv[1]
comurl=url+term
response=urllib2.urlopen(comurl)
print response.read()
