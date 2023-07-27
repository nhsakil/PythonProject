import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>007</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
stuffList = stuff.findall('users/user')
print("User Count: ", len(stuffList))

for user in stuffList:
    print("Name:", user.find('name').text)
    print("ID", user.find('id').text)
    print("Attribute:", user.get("x"))

data = ET.fromstring(data)
print("Name: ", data.find('name').text)
print("Attribute:", data.find("email").get("hide"))
