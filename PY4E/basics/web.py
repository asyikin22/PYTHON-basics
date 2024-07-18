print('hello')

#Serialize XML
import xml.etree.ElementTree as ET
input = ''' 
<stuff>
    <user x="Director">
        <id>01</id>
        <name>Asyikin</name>
    </user>

    <user x="Manager">
        <id>02</id>
        <name>Liam</name>
    </user>
</stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))

#Parse JSON data into Python dictionary - one dictionary
import json
data = '''{
    "name" : "Asyikin",
    "phone" : {
        "type": "international",
        "number": "123 456 789"
        },
    "email": {
        "hide": "yes"}
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Number:', info["phone"]["number"])
print('Hide info:' , info["email"]["hide"])

#parse  JSON data into Python dictionaries - 2 dictionaries
import json
input = '''[
    { "id": "05",
       "y": "HR executive",
       "name": "Lily"
    },
    { "id": "07",
       "y": "Contractor",
       "name": "Austin"
    },
    { "id": "03",
       "y": "Data Analyst",
       "name": "Liam"
    }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute', item['y'])