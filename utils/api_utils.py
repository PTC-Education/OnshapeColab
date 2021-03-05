###############################################################################  
# Project name: Onshape Transformations
# File name: api_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions for reading in parameters, and setting up onshape
#    specific API stuff, also includes general API call function
# Credits/inspirations: API calls referenced from Daniel Ryaboshapka @drybell
# History: 
#    Last modified by Teo 3/3/21
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
# (C) PTC Education
###############################################################################

from onshape_client.client import Client
import json

urls = {
        'create-feature-studio':
            ['POST', '/api/featurestudios/d/did/w/wid'],
        'assembly-definition':
            ['GET', '/api/assemblies/d/did/w/wid/e/eid'],
# ?includeMateFeatures=OPT1&includeNonSolids=OPT2e&includeMateConnectors=OPT3
        'occurrence-transforms':
            ['POST','/api/assemblies/d/did/w/wid/e/eid/occurrencetransforms'],
        'feature-list':
            ['GET', '/api/partstudios/d/did/w/wid/e/eid/features'], #?noSketchGeometry=false
        'add-feature':
            ['POST', '/api/partstudios/d/did/w/wid/e/eid/features'],
        'get-config':
            ['GET', '/api/elements/d/did/w/wid/e/eid/configuration'],
        'set-config':
            ['POST', '/api/elements/d/did/w/wid/e/eid/configuration']
}

#############################################
#                                           #
#   Parsing Args and Connecting to Client   #
#                                           #
#############################################

## TODO: Please find a better solution for global variables than a dictionary
args = {
    "base": None,
    "did": None,
    "wid": None,
    "eid": None,
    "key": None,
    "secret":None,
    "client": None,
    "headers": None
}


# setArgs() - sets the global variables needed for connecting to the client
# Parameters:
#   did - the document's did as a string
#   wid - the document's wid as a string
#   eid - the document's eid as a string
#   base (optional) - the document's base url as a string
#   verbose (optional) - boolean if the user wants to print their document
#      identifiers
# Returns:
#   Nothing
def setArgs(did, wid, eid, base=None, verbose=False):
    if(base):
        args["base"] = base
    args["did"] = did
    args["wid"] = wid
    args["eid"] = eid

    if len(did) != 24:
        print("***Please double check your did! Downstream errors are likely. A client will still be made.***")
    if len(wid) != 24:
        print("***Please double check your wid! Downstream errors are likely. A client will still be made.***")
    if len(eid) != 24:
        print("***Please double check your did! Downstream errors are likely. A client will still be made.***")

    if (not base):
        args["base"] = "https://cad.onshape.com"
        print(". . . Defaulting to cad.onshape.com . . .")

    if(verbose):
        print("Using Workbench:", args["base"])
        print("Document ID:", args["did"])
        print("Workspace ID:", args["wid"])
        print("Element ID:", args["eid"])
        print()

    ## TODO:
    # hit api and check if did, wid, and eid are valid
    # right now checkArgs only prints args


# setKeys() - sets the global variables access and secret key for connecting
#    to the client
# Parameters:
#   access - the user's access key
#   secret - the user's secret key
# Returns:
#   Nothing
def setKeys(access, secret):
    args["key"] = access
    args["secret"] = secret


# connectToClient() - uses clobal variables to connect to Onshape's Python
#    API client
# Parameters:
#   verbose (optional) - Boolean for if the user wants confirmation of a
#    of connection
# Returns:
#   Nothing
def connectToClient(verbose=False):
    # Setting up the client
    args["client"] = Client(configuration={"base_url": args["base"],
                                "access_key": args["key"],
                                "secret_key": args["secret"]})
    args["headers"] = {'Accept': 'application/vnd.onshape.v1+json; charset=UTF-8;qs=0.1',
            'Content-Type': 'application/json'}

    if(verbose):
        print("Connected to Onshape Client!", end="\n\n")



#############################################
#                                           #
#              Making API calls             #
#                                           #
#############################################

# callAPI() - Calls the Onshape API
# Parameters:
#   endpoint - a key from the urls table
#   params   - an empty dictionary (wip)
#   payload  - request body, in json format
# Returns:
#   The response data object from the api call
def callAPI(endpoint, params, payload, hasReturn):

    method    = urls[endpoint][0]
    fixed_url = urls[endpoint][1]
    fixed_url = fixed_url.replace('did', args["did"])
    fixed_url = fixed_url.replace('wid', args["wid"])
    fixed_url = fixed_url.replace('eid', args["eid"])
    # if (endpoint == 'assembly-definition'):
    #   fixed_url = fixed_url.replace('OPT1', "true") # Mate Features
    #   fixed_url = fixed_url.replace('OPT2', "true") # Non Solids
    #   fixed_url = fixed_url.replace('OPT3', "true") # Mate Connectors

    response = args["client"].api_client.request(method, url=args["base"] + fixed_url,
        query_params=params, headers=args["headers"], body=payload)

    # print(response.data)
    if (hasReturn):
    	return json.loads(response.data)
