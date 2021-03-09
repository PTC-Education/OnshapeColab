###############################################################################  
# Project name: Onshape Transformations
# File name: onshape_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions for specific onshape API calls; uses api_utils.py
# History: 
#    Last modified by Teo 3/3/21
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
# (C) PTC Education
###############################################################################
from .utils import api_utils as api
import json

from onshape_client.oas.exceptions import ApiException

def getDocumentInfo(verbose=False):
    payload = {}
    params = {}
    
    try:
        response = api.callAPI('document-info', params, payload, True, didOnly=True)
    except ApiException as error:
        api.printAsError("Check your did, access, and secret keys have been entered correctly!")
        print("Sever message:", error.body)
        print("Ending. . .")
        exit();

    if (verbose):
        print(json.dumps(response, indent=2))

    return response

# connectToOnshape() - The catch all function for making the initial connection
#   to the Onshape Python API client
# Parameters:
#   did - The document's did
#   wid - The document's wid
#   eid - The document's eid
#   access - The user's access key
#   secret - The user's secret key
#   base (optional) - The user's workspace
#   verbose (optional) - Boolean value if the user wants maxmium information
# Returns:
#   Nothing (However this is necessary to run to connect to the API)
def connectToOnshape(did, wid, eid, access, secret, base=None, verbose=False):
    api.setArgs(did, wid, eid, base=base, verbose=verbose)
    api.setKeys(access, secret)
    api.connectToClient(verbose=verbose)
    docInfo = getDocumentInfo()

    print("Retrieved document information:")
    print("\tDocument Name:", docInfo["name"])
    print("\tDocument Owner:", docInfo["owner"]["name"])

    if wid != docInfo["defaultWorkspace"]["id"]:
        print("Note: The wid provided is not the default workspace for the document!")

    if eid != docInfo["defaultElementId"]:
        print("Note: The eid provided is not the default for the document!")
    


#############################################
#                                           #
#             Assembly API Call             #
#                                           #
#############################################

# getAssemblyInfo() - Calls 'assembly-definition' and returns a part and
#      position list
# Parameters:
#   verbose - boolean for excessive print statements
# Returns:
#   - see below

# ## Return Data Structure: a dict of part-objects with their id as the key
#     assemblyReturn = {
#         part_id : {
#             "fullId": [], (eg. ['MFiKjKEzvWtOlyZzO'])
#             "position": [], # transformation matrix
#             "partName": "" (eg. 'Part 1 <1>')
#             "type": "" (eg. 'Part')
#         }
#     }
def getAssemblyInfo(verbose=False):
    payload = {}
    params = {}

    response = api.callAPI('assembly-definition', payload , params, True)

    assemblyReturn = {}

    ### Gets Positions and Paths
    for occurrence in response["rootAssembly"]["occurrences"]:
        # Creates each part-object
        part = {
            "fullPath": occurrence["path"],
            "position": occurrence["transform"],
            "partName": "",
            "type": ""
        }
        assemblyReturn[occurrence["path"][len(occurrence["path"])-1]] = part
        

    ### Gets Part Names and Part Types
    if (verbose):
        print("Parts in assembly:")

    for instance in response["rootAssembly"]["instances"]:
        if(verbose): print("  ", instance["id"], ":", instance["name"])
        assemblyReturn[instance["id"]]["partName"] = instance["name"]
        assemblyReturn[instance["id"]]["type"] = instance["type"]
    
    # Now Prints individual parts in subassemblies!
    for assembly in response["subAssemblies"]:
        for instance in assembly["instances"]:
            if(verbose): print("  ", instance["id"], ":", instance["name"])
            assemblyReturn[instance["id"]]["partName"] = instance["name"]
            assemblyReturn[instance["id"]]["type"] = instance["type"]
    if(verbose): print()

    
    # Debug Printing
    # for partID in assemblyReturn:
    #     print(partID)
    #     # print("\t", assemblyReturn[partID])
    #     print("\t", assemblyReturn[partID]["fullId"])
    #     print("\t", assemblyReturn[partID]["position"])
    #     print("\t", assemblyReturn[partID]["partName"])
    #     print("\t", assemblyReturn[partID]["type"])

    return assemblyReturn

#############################################
#                                           #
#       Occurence Transforms API Call       #
#                                           #
#############################################


# postTransform() - Calls 'occurence-transforms'
# Parameters:
#   M - a transform matrix
#   isRelative - boolean for if the transform is relative
#   parts - an array of part names to apply the transformation to
#   verbose - boolean for excessive print statements
# Returns:
#   Nothing (success code)
def postTransform(M, isRelative, parts, verbose=False):
    
    payload = {
        "occurrences": [],
        "transform": M,                          
        "isRelative": isRelative
    }

    for part in parts:
        occurance = {
            "path": part
        }
        payload["occurrences"].append(occurance)
    # print(json.dumps(payload, indent = 2)) # debugging for printing payload

    if (verbose): print(payload)
    params = {}

    try:
        response = api.callAPI('occurrence-transforms', params, payload, False)
    except ApiException as error:
        print("Invalid transform!")
        print("Sever message:", error.body)
        print("Ending. . .")
        exit();

    return "success"


#############################################
#                                           #
#          Configurations API Call          #
#                                           #
#############################################


# getConfigurations() - Calls 'get-config'
# Parameters:
#   verbose (optional) - boolean for excessive print statements
# Returns:
#   a configurations body (straight from the api)
def getConfigurations(verbose=False):
    payload = {}
    params = {}
    
    try:
        response = api.callAPI('get-config', params, payload, True)
    except ApiException as error:
        print("Invalid transform!")
        print("Sever message:", error.body)
        print("Ending. . .")
        exit();

    if (verbose):
        print(response)

    return response



# setConfigurations() - Calls 'set-config'
# Parameters:
#   toSet - a dictionary where key:parameterId, values: default/min/max
#   configInfo - configuration body from getConfigurations()
#   verbose - boolean for excessive print statements
# Returns:
#   Nothing (success code)
def setConfigurations(toSet, configInfo ,verbose=False):
    
    payload = configInfo
    params = {}

    if len(toSet) > 0:
        for config in configInfo["configurationParameters"]:
            if config["message"]["parameterId"] in toSet:

                # print("Config:", config["message"]["parameterId"])
                # print("\tBefore:", config["message"]["rangeAndDefault"]["message"]["defaultValue"])
                # print("\tAfter:", toSet[config["message"]["parameterId"]])

                currentConfig = config["message"]["rangeAndDefault"]["message"]
                currentConfig["defaultValue"] = toSet[config["message"]["parameterId"]]
                currentConfig["minValue"] = toSet[config["message"]["parameterId"]]
                currentConfig["maxValue"] = toSet[config["message"]["parameterId"]]

        if verbose: print(json.dumps(payload, indent = 2))
        
        try:
            response = api.callAPI('set-config', params, payload, False)
        except ApiException as error:
            print("Invalid transform!")
            print("Sever message:", error.body)
            print("Ending. . .")
            exit();
    else:
        if verbose: print("The 'toSet' dictionary was empty so the API was not called.")

    return "success"
