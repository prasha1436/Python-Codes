import urllib.request
from bs4 import BeautifulSoup as bs4

url= input('Enter the url: ')
xmlstr= urllib.request.urlopen(url).read()
soupo= bs4(xmlstr, 'xml')
#print(soupo)

tags= soupo('count')
sum= 0
print(tags)
for entry in tags:
    counttxt= entry.text
    countint= int(counttxt)
    sum= sum + countint

print(sum)
