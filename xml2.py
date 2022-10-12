import xml.etree.ElementTree as ET

i= '''<userdatabase>
        <users>
            <user x="2">
                <id>007</id>
                <name>Bond</name>
            </user>
            <user x="420">
                <id>101</id>
                <name>Prasha</name>
            </user>
        </users>
        </userdatabase>'''

treee= ET.fromstring(i)
t= treee.findall('users/user')
for obj in t:
    print(obj.get('x'))
    print(obj.find('name').text)
    print(obj.find('id').text)
