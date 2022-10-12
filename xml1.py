import xml.etree.ElementTree as ET

i= '''
    <person>
        <name>Prasha</name>
        <phone type= "intl">
9500181654</phone>
        <email hide= "yes"/>
    </person>'''

t= ET.fromstring(i)
print(t.find('name').text)
print(t.find('phone').get('type'), t.find('phone').text)
print(t.find('email').get('hide'))
