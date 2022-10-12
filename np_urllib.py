import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand= urllib.request.urlopen('http://data.pr4e.org/page1.htm')

for l in fhand:
    print(l.decode().rstrip())
