import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = ("http://py4e-data.dr-chuck.net/comments_1843129.html")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

# Retrieve all the <span> tags with class="comments"
tags = soup.find_all('span', class_='comments')

#retrive all the anchor tags
tagsnumbers = list()
tags = soup('span') #Anchor tags
for tag in tags:
    tagsnumbers.append(int(tag.text))
print(sum(tagsnumbers))
