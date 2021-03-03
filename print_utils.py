from .utils import transform_utils as transform


def printConfigurations(configInfo):
    print("Configurations:")
    for config in configInfo["configurationParameters"]:
        print(config["message"]["parameterId"])
        try:
            print("\tDefault value: ",
                config["message"]["rangeAndDefault"]["message"]["defaultValue"])
            print("\tMax value: ",
                config["message"]["rangeAndDefault"]["message"]["maxValue"])
            print("\tMin value: ",
                config["message"]["rangeAndDefault"]["message"]["minValue"])
        except:
            print("There are no values for this configuration.")

def printAssembly(assemblyInfo, positions=False):
    print("Assembly Info:")
    for identifier in assemblyInfo:
        print(assemblyInfo[identifier]["partName"], "(" + identifier + ")")
        if positions:
            transform.decodeMatrix(assemblyInfo[identifier]["position"], True)
    print()