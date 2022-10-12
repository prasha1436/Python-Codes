import urllib.request
from bs4 import BeautifulSoup as bs4

url= input('Enter the url:')
countstr= input('Enter Count:')
count= int(countstr)
posstr= input('Enter the position:')
pos= int(posstr)
lst= list()
for i in list(range(count)):
    htmlstr= urllib.request.urlopen(url).read()
    print('Retrieving:', url)
    soupo= bs4(htmlstr, 'html.parser')
    #print(soupo)
    tags= soupo('a')
    url= tags[pos-1].get('href')
    lst.append(tags[pos-1].text)

print(lst)
