import urllib.request
from bs4 import BeautifulSoup as bs4

url = input('Enter the website-')
html1= urllib.request.urlopen(url).read()
refhtml= bs4(html1, 'html.parser')

tags= refhtml('a')
print(html1)
print(refhtml)
print(tags)
for tag in tags:
    print(tag.get('href', '-1'))
    print(tag.text)
