###############################################################################  
# Project name: OnshapeColab
# File name: print_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 3/3/2021
# Description: Functions for easy printing
# History: 
#    Last modified by Teo 3/3/2021
# (C) PTC Education
###############################################################################
from .utils import transform_utils as transform

# printConfigurations() - Prints information from a configurationInfo body (as
#     returned from getConfigurations())
# Parameters:
#   configInfo - configuration information to be printed
#   values (optional) - boolean for if the user wants to print the current
#    values of the configurations
# Returns:
#   Nothing
def printConfigurations(configInfo, values=True):
    print("Configurations:")
    for config in configInfo["configurationParameters"]:
        print(config["message"]["parameterId"])
        if values:
            try:
                print("\tDefault value: ",
                    config["message"]["rangeAndDefault"]["message"]["defaultValue"])
                print("\tMax value: ",
                    config["message"]["rangeAndDefault"]["message"]["maxValue"])
                print("\tMin value: ",
                    config["message"]["rangeAndDefault"]["message"]["minValue"])
            except:
                print("There are no values for this configuration.")
    print()


# printAssembly() - Prints information from an assemblyInfo body (as described
#     in onshape_utils)
# Parameters:
#   assemblyInfo - data strcture returned from getAssemblyInfo, information to
#    be printed
#   positions (optional) - boolean for if the user wants the positions of the
#    parts in the assembly to be printed
# Returns:
#   Nothing
def printAssembly(assemblyInfo, positions=False):
    print("Assembly Info:")
    for identifier in assemblyInfo:
        print(assemblyInfo[identifier]["partName"], "(" + identifier + ")")
        if positions:
            transform.decodeMatrix(assemblyInfo[identifier]["position"], True)
    print()