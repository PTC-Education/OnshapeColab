###############################################################################  
# Project name: Onshape Transformations
# File name: api_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions for reading in parameters, and setting up onshape
#    specific API stuff, also includes general API call function
# Credits/inspirations: API calls referenced from Daniel Ryaboshapka @drybell
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
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

arg = {
    "base": None,
    "did": None,
    "wid": None,
    "eid": None,
    "key": None,
    "secret":None
}

def setArgs(did, wid, eid, base=None):
    if(base):
        arg["base"] = base
    arg["did"] = did
    arg["wid"] = wid
    arg["eid"] = eid

    if (base):
        arg["base"] = "https://cad.onshape.com"
        print(". . . Defaulting to cad.onshape.com . . .")

# checkArgs() - Validates the did, wid, and eid
# Parameters:
#   verbose - boolean for excessive print statements
# Returns:
#   Nothing (wip)
def checkArgs(verbose):
    if(verbose):
        print("Using Workbench:", arg["base"])
        print("Document ID:", arg["did"])
        print("Workspace ID:", arg["wid"])
        print("Element ID:", arg["eid"])
        print()
    
    ## TODO:
    # hit api and check if did, wid, and eid are valid
    # right now checkArgs only prints args



def setKeys(access, secret):
    arg["key"] = access
    arg["secret"] = secret

def connectToClient():
    # Setting up the client
    client = Client(configuration={"base_url": arg["base"],
                                "access_key": arg["key"],
                                "secret_key": arg["secret"]})
    headers = {'Accept': 'application/vnd.onshape.v1+json; charset=UTF-8;qs=0.1',
            'Content-Type': 'application/json'}




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
    fixed_url = fixed_url.replace('did', arg["did"])
    fixed_url = fixed_url.replace('wid', arg["wid"])
    fixed_url = fixed_url.replace('eid', arg["eid"])
    # if (endpoint == 'assembly-definition'):
    #   fixed_url = fixed_url.replace('OPT1', "true") # Mate Features
    #   fixed_url = fixed_url.replace('OPT2', "true") # Non Solids
    #   fixed_url = fixed_url.replace('OPT3', "true") # Mate Connectors

    response = client.api_client.request(method, url=arg["base"] + fixed_url,
        query_params=params, headers=headers, body=payload)

    # print(response.data)
    if (hasReturn):
    	return json.loads(response.data);
