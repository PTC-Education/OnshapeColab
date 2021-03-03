
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