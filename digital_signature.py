import json

import nacl.signing
import nacl.encoding

print("")
print("Keys")
print("----")

signing_key = nacl.signing.SigningKey.generate()

verify_key = signing_key.verify_key

print(f"Signing key is: {signing_key.encode(encoder=nacl.encoding.HexEncoder).decode('utf-8')}")
print(f"Verify key is: {verify_key.encode(encoder=nacl.encoding.HexEncoder).decode('utf-8')}")

print("")
print("Transaction")
print("-----------")

sender = input("Enter sender: ")

recipient = input("Enter recipient ")

amount = int(input("Enter amount: "))

transaction = (sender, recipient, amount)

print("")
print(f"Transaction is: {transaction}")

converted = json.dumps(transaction)

encoded_transaction = converted.encode('utf-8')

print("")
print("Signature")
print("---------")

signed_transaction = signing_key.sign(encoded_transaction)

print(f"Signature is: {signed_transaction.signature.hex()}")

print("")
print("Auth")
print("----")

signature = bytes.fromhex(input("Enter signature to validate: "))

def verify(key, message, sig):
    try:
        key(message,sig)
        print("Signature valid")
    except:
        print("Signature invalid")

print("")
verify(verify_key.verify, encoded_transaction, signature)
print("")