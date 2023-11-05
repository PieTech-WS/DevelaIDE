with open("./source/org.cora.mod.pe.tar", "b+r") as a:
    byte = a.read()

import hashlib
print(hashlib.md5(byte).hexdigest())