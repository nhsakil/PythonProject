# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that
# is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py
# Make sure to check that your code is using the API endpoint is as shown above.
# Please run your program to find the place_id for this location: University of Akron
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJbye ..."


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

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
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    pid = js['results'][0]['place_id']
    print('Place id ',pid)