
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

# promtConfigurations() - Asks user if they would like to edit configurations
#   from a given configInfo
# Parameters:
#   configInfo - a dictionary returned from getConfigurations()
# Returns:
#   A  dictionary containing configuration names and their new desired values
def promptConfigurations(configInfo):
    newConfigs = {}
    print("What Configurations do you want to edit?")
    for config in configInfo["configurationParameters"]:
        query = "\tEdit {field}?".format(field = config["message"]["parameterId"])
        if (promptUser(query)):
            
            try:
                print("Current default value: ", config["message"]["rangeAndDefault"]["message"]["defaultValue"])
                print("\tEnter new value:")#, endl="\n\t")
                inputVal = input()

                try:
                    newVal = int(inputVal)
                    newConfigs[config["message"]["parameterId"]] = newVal
                except:
                    print("A non-integer value was entered. The configuration will not be added.")

            except:
                print("This value is not setable.")
    return newConfigs
    
def promptThings(thingworxGet):
    newThings = {}
    print("What Thing fields do you want to edit?")
    for field in thingworxGet:
        query = "\tEdit {}?".format(field)
        if (promptUser(query)):
            
            try:
                print("Current default value: ", thingworxGet[field])
                print("\tEnter new value:")#, endl="\n\t")
                inputVal = input()

                try:
                    newVal = int(inputVal)
                    newThings[field] = newVal
                except:
                    print("A non-integer value was entered. The field will not be added.")

            except:
                print("This value is not setable.")
    return newThings
    