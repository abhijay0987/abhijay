%%time
%%memit
import sys
import hashlib
if sys.version_info < (3, 6): import sha3
print("............SHA3-512 Implementation............\n")
data = input("Enter the data: ")
print("\n\nOriginal data: ", data)
23
# create an sha3 hash object
hash_sha3_512 = hashlib.new("sha3_512", data.encode())
print("\nAfter applying Hash Function:\n",hash_sha3_512.hexdigest())
