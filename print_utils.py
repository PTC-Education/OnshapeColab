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

# printConfigurations() - Prints information from a configurationInfo body (as
#     returned from getConfigurations())
# Parameters:
#   configInfo - configuration information to be printed
#   values (optional) - boolean for if the user wants to print the current
#    values of the configurations
# Returns:
#   Nothing
def printConfigurations(configInfo, values=True):
    if len(configInfo["configurationParameters"]) > 0:
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
    else:
        print("There are no set configurations for this document.")
    print()


