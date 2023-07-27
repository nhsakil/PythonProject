import xml.etree.ElementTree as ET

import urllib.request, urllib.parse, urllib.error

url = input("Enter the url")
fileHandle = urllib.request.urlopen(url).read().decode()

stuff = ET.fromstring(fileHandle)

tags = stuff.findall('comments/comment')
countslist = list()

for tag in tags:
    tag = int(tag.find('count').text)
    countslist.append(tag)
print(sum(countslist))
