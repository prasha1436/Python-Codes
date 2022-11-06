import urllib.request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs4

url= input('Enter the url: ')
xmlstr= urllib.request.urlopen(url).read()
soupo= bs4(xmlstr, 'xml')
t= ET.fromstring(xmlstr)
#print(soupo)

tags= soupo('count')
#tags= t.findall('.//count')
sum= 0
print(tags)
for entry in tags:
    counttxt= entry.text
    countint= int(counttxt)
    sum= sum + countint

print(sum)
