###############################################################################  
# Project name: Thingworx utils
# File name: thingworx_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 10/16/20
# Description: Functions for reading and writing to thingworx
# History: 
#    Last modified by Teo 10/16/20
###############################################################################

import requests,json # packages for Thingworx POST & GET

TWargs = {
    "url": None,
    "appKey": None,
    "headers": {
        'AppKey': appKey,
        'Accept': "application/json",
        'Content-Type': "application/json"
        }
}

def setTWArgs(url, appKey):
    TWargs["url"] = url
    TWargs["appKey"] = appKey


def connectToThingwox(url, appKey, verbose=False):
    setTWArgs(url, appKey)
    fields = thingworxGET()
    for field in fields:
        print(field)


#############################################
#                                           #
#            GET and POST requests          #
#                                           #
#############################################

# thingworxGET() - acts as a GET request to the thingworx dashboard in the 
#   thingworx-keys file 
# Parameters:
#   fields - an array of fields wanted from the dashboard
# Returns:
#   - a dictionary where the parameter fields are the keys and the thingworx
#      values are the keys
def thingworxGET(fields={}):
    body = requests.get(TWargs["url"],headers=TWargs["headers"]).json()
    data = {}

    if fields:
        for field in fields:
            data[field] = body["rows"][0][field]
    else:
        for field in body["rows"][0]:
            data[field] = body["rows"][0][field]
        ## WARNING: Untested

    return data



# thingworxPUT() - acts as a PUT request to the thingworx dashboard in the
#   thingworx-keys file
# Parameters:
#   setValues - a dictionary of values to be set in the thingworx dashboard
# Returns:
#   - nothing
def thingworxPUT(setValues):
  return requests.put(TWargs["url"],headers=TWargs["headers"],json=propValue)