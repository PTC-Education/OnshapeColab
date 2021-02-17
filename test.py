# !pip3 install -r requirements.txt 

import utils.onshape_utils as onshape
import utils.api_utils as api

did = "688d52d4b40fa464e65b9335"
wid = "9399f9d1b4a559d90a2ac87a"
eid = "c9a50713ea054cf8b1803b2c"

access = "DMq7FljpquvzkaoXdLTlRvLY"
secret = "fE7W1fcL40v4JoLuNJQ7VbFXquEbzFELurr1NmB7MAcAOku8"

# access = [access key]
# secret = [secret key]

onshape.connectToOnshape(did, wid, eid, access, secret, verbose=True)
## TODO: test with base and secret

# api.setArgs(did, wid, eid)
# api.setKeys(access, secret)
# api.connectToClient(verbose=True)

assemblyInfo = onshape.getAssemblyInfo(True)
