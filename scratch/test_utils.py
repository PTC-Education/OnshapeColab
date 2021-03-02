arg = {
    "base": None,
    "did": None,
    "wid": None,
    "eid": None,
    "key": None,
    "secret": None
}

def setArgs(did, wid, eid, base=None):
    if(base):
        arg["base"] = base
    arg["did"] = did
    arg["wid"] = wid
    arg["eid"] = eid

    if (base):
        arg["base"] = "https://cad.onshape.com"
        print(". . . Defaulting to cad.onshape.com . . .")

def checkArgs(verbose):
    if(verbose):
        print("Using Workbench:", arg["base"])
        print("Document ID:", arg["did"])
        print("Workspace ID:", arg["wid"])
        print("Element ID:", arg["eid"])
        print()





