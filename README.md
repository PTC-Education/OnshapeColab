# Onshape API Playground: transformations and configurations
This playground was adapted from a previously made repo: https://github.com/imnotartsy/Onshape-Connections

## Purpose
This repository is intended to be used with an external file which references the utility functions here. Its intent is to make powerful features of the Onshape API accessible.

# Table of Contents
- Getting Started Documentation
  - [Onshape API Keys](https://github.com/PTC-Education/PTCColab#onshape-api-keys)
  - [Thingworx Keys](https://github.com/PTC-Education/PTCColab#thingworx-if-being-used)
- Function Documentation
  - Onshape Connection / [Connect to Onshape](https://github.com/PTC-Education/PTCColab#connecttoonshape)
    - Information Queries
        - [GET Document Information](https://github.com/PTC-Education/PTCColab#getdocumentinfo)
        - [GET Part Information](https://github.com/PTC-Education/PTCColab#getparts)
        - [GET Meta Data](https://github.com/PTC-Education/PTCColab#getmeta)
    - Assemblies and Transforms
        - [GET Assembly Information](https://github.com/PTC-Education/PTCColab#getassemblyinfo)
        - [PRINT Assembly Information](https://github.com/PTC-Education/PTCColab#printassembly)
        - [POST Transform](https://github.com/PTC-Education/PTCColab#posttransform)
    - Transform Matricies and Transform Args ([tx, ty, tx, rx, ry, rz, w])
        - [GET Transformation Matrix](https://github.com/PTC-Education/PTCColab#gettranslationmatrix)
        - [GET Transformation Arg/Decode Matrix](https://github.com/PTC-Education/PTCColab#decodematrix)
        - [Multiply Transformation Matrices](https://github.com/PTC-Education/PTCColab#multiply)
        - [Add Transformation Matrices](https://github.com/PTC-Education/PTCColab#add)
        - [PRINT Transformation Matrix](https://github.com/PTC-Education/PTCColab#prettyprintmatrix)
        - [PRINT Transformation Arg](https://github.com/PTC-Education/PTCColab#prettyprintposition)
    - Configurations
        - [GET Configurations](https://github.com/PTC-Education/PTCColab#getconfigurations)
        - [POST Configurations](https://github.com/PTC-Education/PTCColab#setconfigurations)
        - [PRINT Configurations](https://github.com/PTC-Education/PTCColab#printconfigurations)
        - [Prompt Configurations](https://github.com/PTC-Education/PTCColab#promptconfigurations)
  - Thingworx Connection / [Connect to Thingworx](https://github.com/PTC-Education/PTCColab#connecttothingworxurl-appkey-verbosefalse)
    - [GET Thingworx Fields and Properties](https://github.com/PTC-Education/PTCColab#thingworxget)
    - [PUT Thingworx Properties](https://github.com/PTC-Education/PTCColab#thingworxput)



# Getting Started
## Onshape API Keys
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

## Thingworx (if being used)
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

Example call: 
```
oc.connectToOnshape(did, wid, eid, access, secret, verbose=True)
```

Example print to output:
```
. . . Defaulting to cad.onshape.com . . .
Using Workbench: https://cad.onshape.com
Document ID: d75bb6f0855244bdb3902141
Workspace ID: 2a59db92740eb894f3b29038
Element ID: 3bddbc17e620a65192e913f8

Connected to Onshape Client!
```


### ```getDocumentInfo()```

Parameters:
  - verbose (optional) - boolean for printing the raw response from the Onshape API

Returns:
  - raw response from getDocumentInfo API call (this is generally used in conjuction with `connectToOnshape()`) which automatically parses the data.


Example call:
```
documentInfo = oc.getDocumentInfo(verbose=True)
```


### ```getParts()```
  Calls 'parts' and returns a dictionary of part names and associated pids and eids

Parameters:
  - verbose (optional) - boolean for printing the raw response

Returns:
  - a dictionary of part names and associated pids and eids

Example call:
```
parts = oc.getParts()
```

Example return:
```
{
  "Plane": {
    "pid": "JHD",
    "eid": "42bbbd1df82e9fb4a7163114"
  },
  "Key": {
    "pid": "JID",
    "eid": "42bbbd1df82e9fb4a7163114"
  },
  "box": {
    "pid": "JHD",
    "eid": "849ac855fd55f14317980bd0"
  }
}
```

### ```getMeta()```
Calls 'get-metadata' and returns the raw response

Parameters:
  - eid - element id containing the part
  - pid - the part id of the specified part
  - verbose (optional) - a boolean for printing the raw respomse 

Returns: 
  - the raw response from 'get-metadata'

Example Call:
```
WIP
```

Example Return:
```
WIP
```

### ```postMeta()```
Calls 'post-metadata' and posts . . . WIP

Parameters:
  - WIP
Returns:
  - WIP

Example Call:
```
WIP
```

Example Return:
```
WIP
```


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

Example call:
```
assemblyInfo = oc.getAssemblyInfo()
```

Example return:
```
assemblyInfo = 
{
  'M1YqtB8Y6W/lPi9Ug':
  {
    'fullPath': ['M1YqtB8Y6W/lPi9Ug'],
    'position': [1.000,      1.665e-16,  1.187e-17, -3.490e-19,
                 1.129e-17, -6.915e-16, -1.000,     -0.005,
                -5.989e-32,  1.000,     -6.322e-16, -0.003,
                 0.0,        0.0,        0.0,        1.0],
    'partName': 'Hour Hand <3>',
    'type': 'Part'
  },
  'MSIp2OzuDBEJzDhb5':
  {
    'fullPath': ['MSIp2OzuDBEJzDhb5'],
    'position': [1.000,     -3.330e-16,  2.622e-17,  1.210e-18,
                -2.465e-32, -2.414e-16, -0.999,     -0.006,
                 0.0,         1.000,    -2.029e-16, -0.003,
                 0.0,           0.0,     0.0,        1.0],
    'partName': 'Second Hand <4>',
    'type': 'Part'
  }
}
```
Note: The values inside position have been truncated for formatting




### ```postTransform()```
Calls 'occurence-transforms' endpoint

Parameters:
  - M - a transform matrix
  - isRelative - boolean for if the transform is relative
  - parts - an array of part names to apply the transformation to
  - verbose - boolean for excessive print statements

Returns:
  - Nothing (success code)

Example call:
```
oc.postTransform(M, True, parts)
```

Example print:
```
'success'
```

Example return:
```
"success"
```
or other status code.

### ```getConfigurations()```
Calls 'get-config'

Parameters:
  - verbose (optional) - boolean for excessive print statements

Returns:
  - a configurations body (straight from the api)

Example call:
```
oc.getConfigurations()
```

Example return:
This return is never meant to be used directly. It is meant to be passed between functions and never be printed.

### ```setConfigurations()```
Calls 'set-config'
Parameters:
  - toSet - a dictionary where key: parameterId, values: default/min/max
  - configInfo - configuration body from getConfigurations()
  - verbose - boolean for excessive print statements

Returns:
  - Nothing (success code)

Example call:
```
oc.setConfigurations(newConfigs, configInfo)
```

Example print:
```
'success'
```

## File: ```print_utils.py```
### ```printConfigurations()```
Prints information from a configurationInfo body (as returned from getConfigurations())

Parameters:
  - configInfo - configuration information to be printed
  - values (optional) - boolean for if the user wants to print the current values of the configurations
  
Returns:
  - Nothing

Example call:
```
oc.printConfigurations(configInfo)
```

Example print:
```
Configurations:
Rotation
	Default value:  0.0
	Max value:  0.0
	Min value:  0.0
HourRotation
	Default value:  0.0
	Max value:  0.0
	Min value:  0.0
SecondRotation
	Default value:  0.0
	Max value:  0.0
	Min value:  0.0
```


## ```input_utils.py```
### ```readInTransformObject```
reates transform args objects (as defined above)

Parameters:
  - None

Returns:
  - A transform args object

  Example call:
```
WIP
```

Example print:
```
WIP
```

Example return:
```
WIP
```

### ```promtUser()```
Asks user a query string that has a yes or no answer

Parameters:
  - queryString - The question for the user

Returns:
  - A boolean value depending on the user's input

  Example call:
```
WIP
```

Example print:
```
WIP
```

Example return:
```
WIP
```

### ```promptConfigurations()```
Asks user if they would like to edit configurations from a given configInfo

Parameters:
  - configInfo - a dictionary returned from getConfigurations()

Returns:
  - A  dictionary containing configuration names and their new desired values

Example call:
```
newConfigs = oc.promptConfigurations(configInfo)
```

Example print:
```
What Configurations do you want to edit?
	Edit Rotation? (y/n)
y
Current default value:  0.0
	Enter new value:
180
	Edit HourRotation? (y/n)
n
	Edit SecondRotation? (y/n)
n
```

Example return:
```
{
  "Rotation": 180
} 
```


## ```thingworx_utils.py```
This file contains everything pertaining to the connection with ThingWorx


### ```connectToThingworx(url, appKey, verbose=False)```
Sets url and appKey as internal variables for GET and PUT calls

Parameters:
  - url - the dashboard's thing URL
  - appKey - an appKey associated with the thing's dashboard with the necssary permissions
  - verbose (optional) - boolean for printing the avaliable fields

Returns:
  - nothing

Example call:
```
oc.connectToThingworx(url, appKey)
```

Example print:
```
Thingworx fields:
	 name
	 description
	 thingTemplate
	 tags
	 Minute
	 Second
	 Hour
	 HourCopyCopy
	 HourCopy
```


### ```thingworxGET()```
Acts as a GET request to the thingworx dashboard

Parameters:
  - fields - an array of fields wanted from the dashboard

Returns:
  - a dictionary where the parameter fields are the keys and the thingworx
     values are the keys

Example call:
```
fields = oc.thingworxGET()
```

Example print:
```
Fields and Values
	name: TP-TestThing1
	description: Test thing for Onshape Colab
	thingTemplate: GenericThing
	tags: []
	Minute: 0
	Second: 0
	Hour: 90
	HourCopyCopy: 0
	HourCopy: 0
```


### ```thingworxPUT()```
Acts as a PUT request to the thingworx dashboard
Parameters:
  - setValues - a dictionary of values to be set in the thingworx dashboard
Returns:
  nothing

Example call:
```
oc.thingworxPUT(setValues)
```

Example print:
```
<Response [200]>
```

Example return:
```
WIP
```




## ```transforms.py```

### ```printAssembly()```
Prints information from an assemblyInfo body (as described in onshape_utils)

Parameters:
  - assemblyInfo - data strcture returned from getAssemblyInfo, information to be printed
  - positions (optional) - boolean for if the user wants the positions of the parts in the assembly to be printed

Returns:
  - Nothing

Example call:
```
oc.printAssembly(assemblyInfo, positions=True)
```

Example print to output:
```
Assembly Info:
Hour Hand <3> (M1YqtB8Y6W/lPi9Ug)
	**Transform Matrix out of bounds, position may be printed wrong**
	Translation (x, y, z): 		 -0.0 	 -0.006 	 -0.003
	Rotation (ux, uy, uz, alpha): 	 1.41421 	 0.0 	 -0.0 	 45.0
Second Hand <4> (MSIp2OzuDBEJzDhb5)
	Translation (x, y, z): 		 0.0 	 -0.007 	 -0.003
	Rotation (ux, uy, uz, alpha): 	 1.41421 	 0.0 	 0.0 	 45.0
```
Note: "Transform Matrix out of bounds, position may be printed wrong" is a bug warning.

