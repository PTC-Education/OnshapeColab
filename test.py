import test_utils as test

did = "688d52d4b40fa464e65b9335"
wid = "9399f9d1b4a559d90a2ac87a"
eid = "c9a50713ea054cf8b1803b2c"

# access = [access key]
# secret = [secret key]


test.checkArgs(True)
test.setArgs(did, wid, eid)#, base=workspace)
test.checkArgs(True)

