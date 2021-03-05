# Onshape API Playground: transformations and configurations
This playground was adapted from a previously made repo: https://github.com/imnotartsy/Onshape-Connections

## Purpose
This repository is intended to be used with an external file which references the utility functions here. Its intent is to make powerful features of the Onshape API accessible.

# Getting Started
## Onshape
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
[coming soon]

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
[coming soon]

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
