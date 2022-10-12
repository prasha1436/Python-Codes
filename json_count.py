import json
import urllib.request

url= input('Enter the url:')
str= urllib.request.urlopen(url).read()
lst= json.loads(str)['comments']
sum= 0
for items in lst:
    sum = sum + items['count']

print(sum)
