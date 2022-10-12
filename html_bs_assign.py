import urllib.request
from bs4 import BeautifulSoup as bs4

url= input('Enter the url: ')
htmlstr= urllib.request.urlopen(url).read()
soupo= bs4(htmlstr, 'html.parser')
#print(soupo)

tags= soupo('span')
sum= 0
print(tags)
for entry in tags:
    spantxt= entry.text
    spanint= int(spantxt)
    sum= sum + spanint

print(sum)
