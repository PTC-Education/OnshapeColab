# Onshape API Playground: transformations and configurations
This playground was adapted from a previously made repo: https://github.com/imnotartsy/Onshape-Connections

## Purpose
This repository is intended to be used with an external file which references the utility functions here. Its intent is to make powerful features of the Onshape API accessible.

# Getting Started/File System
## Before Running 

### Onshape
- To connect to the Onshape API, an api key and secret are needed.
  - This is done here: https://dev-portal.onshape.com > API Keys > "Create New API Key"
  - Save these in a safe place as they will be needed to use the function ```connectToOnshape()```
    - If the user is using a template, the keys go in the place of "[access key]" and "[secrete key]"
  - Note: You will need separate keys for every different workspace the user plans to work in.
- Then a did, wid, eid, and workspace are needed from the Onshape Workspace.
  - The did, wid, and eid are each 24 character strings found in your Onshape document url.
    - The did is found after "documents/" or "did"
    - The wid is found after "/w/"
    - The eid is found after "/e/"
  - The workspace is the base url, such as "https://cad.onshape.com"
  - The did, wid, eid, and workspace will also be needed for the initial ```connectToOnshape()``` function.

### Thingworx (if being used)
- To connect with a thingworx dashboard, a url and an app key are needed.
  - Put the url and the app key into the file ```thingworx-keys``` (right
  now it has placeholders "[url]" and "[appkey]")


# Common Problems
- [Begin list here]
- Any questions? Shoot me an email tpatro01@tufts.edu

# Function Documentation
## File: ```onshape_utils.py```
These functions are used mainly to make direct api calls such as getting and setting information.

### ```connectToOnshape()```
The catch all function for making the initial connection
  to the Onshape Python API client

Parameters:
  - did - The document's did
  - wid - The document's wid
  - eid - The document's eid
  - access - The user's access key
  - secret - The user's secret key
  - base (optional) - The user's workspace
  - verbose (optional) - Boolean value if the user wants maxmium information

Returns:
  - Nothing (However this is necessary to run to connect to the API)

### ```getAssemblyInfo()```
  Calls 'assembly-definition' and returns a part and position list

Parameters:
  - verbose - boolean for excessive print statements

Returns:
  - see below

Return Data Structure: a dictary with the following fields

Ex.
<pre>
    assemblyReturn = {
        part_id : {
            "fullId": [], (eg. ['MFiKjKEzvWtOlyZzO'])
            "position": [], # transformation matrix
            "partName": "" (eg. 'Part 1 <1>')
            "type": "" (eg. 'Part')
        }
    }</pre>

### ```postTransform()```
Calls 'occurence-transforms' endpoint

Parameters:
  - M - a transform matrix
  - isRelative - boolean for if the transform is relative
  - parts - an array of part names to apply the transformation to
  - verbose - boolean for excessive print statements

Returns:
  - Nothing (success code)

### ```getConfigurations()```
Calls 'get-config'

Parameters:
  - verbose (optional) - boolean for excessive print statements

Returns:
  - a configurations body (straight from the api)

### ```setConfigurations()```
Calls 'set-config'
Parameters:
  - toSet - a dictionary where key: parameterId, values: default/min/max
  - configInfo - configuration body from getConfigurations()
  - verbose - boolean for excessive print statements

Returns:
  - Nothing (success code)

## File: ```print_utils.py```
### printConfigurations()
Prints information from a configurationInfo body (as returned from getConfigurations())

Parameters:
  - configInfo - configuration information to be printed
  - values (optional) - boolean for if the user wants to print the current values of the configurations
  
Returns:
  - Nothing

### ```printAssembly()```
Prints information from an assemblyInfo body (as described in onshape_utils)

Parameters:
  - assemblyInfo - data strcture returned from getAssemblyInfo, information to be printed
  - positions (optional) - boolean for if the user wants the positions of the parts in the assembly to be printed

Returns:
  - Nothing

## ```input_utils.py```
[coming soon]

## ```thingworx_utils.py```
[coming soon]