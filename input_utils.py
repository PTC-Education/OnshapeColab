
#############################################
#                                           #
#            User Input functions           #
#                                           #
#############################################

# readInTransformObject() - Creates transform args objects (as defined above)
# Parameters:
#   None
# Returns:
#   A transform args object
def readInTransformObject():
    args = []
    dim  = ["tx", "ty", "tz", "rx", "ry", "rz", "alpha (degree)"]
    for i in range(0,7):
        print("Please Enter {name} value:".format(name = dim[i]))
        try:
            args.append(float(input()))
        except:
            print("The input entered is not valid. (Ending . . .)")
            exit()
    
    return args


# promtUser() - Asks user a query string that has a yes or no answer
# Parameters:
#   queryString - The question for the user
# Returns:
#   A boolean value depending on the user's input
def promptUser(questionString):
    print(questionString, "(y/n)")
    userIn = input()
    if (userIn.upper() == 'Y' or userIn.upper() == 'YES'):
        return True
    elif (userIn.upper() == 'N' or userIn.upper() == 'NO'):
        return False
    else:
        print("The input entered is not valid.")
        return False

def promptConfigurations(configInfo):
    newConfigs = {}
    print("What Configurations do you want to edit?")
    for config in configInfo["configurationParameters"]:
        query = "\tEdit {field}?".format(field = config["message"]["parameterId"])
        if (promptUser(query)):
            
            try:
                print("Current default value: ", config["message"]["rangeAndDefault"]["message"]["defaultValue"])
                print("\tEnter new value:")
                newVal = input()
                try:
                    newVal = int(newVal)
                    newConfigs[config["message"]["parameterId"]] = newVal;
                except:
                    print("Invalid input for a configurations.")
            except:
                print("This value is not setable.")
    return newConfigs
    