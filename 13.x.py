import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs4
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
#    refdata= bs4(data, 'xml')
    print('Retrieved', len(data), 'characters')
#    print(data)
#    tree = ET.fromstring(data)
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=2))
    print('Place ID:', js['results'][0]['place_id'])
#    results = tree.findall('result')
#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text

#    print('lat', lat, 'lng', lng)
#    print(location)
#    latstr= refdata('lat')
#    lngstr= refdata('lng')
#    print(latstr, lngstr)
#    sum1=0.0
#    sum2=0.0
#       j= float(i.text)
#        sum1= sum1+ j
#    for k in lngstr:
#        l= float(k.text)
#        sum2= sum2+l
#    print(sum1+sum2)
