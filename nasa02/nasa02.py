#!/usr/bin/env python3
import urllib.request
import json

## Define NEOapi 
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2021-02-07'
enddate = '&end_date=END_DATE'
mykey = '&api_key=FBMTDIoxDeBhHjcCdemRRdAYMMlRYC3baoN9Kvf9'    ## your key goes in place of DEMO_KEY

neourl = neourl + startdate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode JSON to Python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(decodeneo)

