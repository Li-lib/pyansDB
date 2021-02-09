#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2021-02-07'  ## start date for data
    enddate = '&end_date=2021-02-09' ## create a mechanism to utilize enddate
    mykey = '&api_key=FBMTDIoxDeBhHjcCdemRRdAYMMlRYC3baoN9Kvf9' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

