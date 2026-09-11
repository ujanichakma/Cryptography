from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.Util.Padding import pad, unpad
import zlib, base64

def b64(data):
    return base64.b64encode(data).decode()

key_a = RSA.generate(2048)
key_b = RSA.generate(2048)
private_key_a = key_a
private_key_b = key_b
public_key_a = key_a.public_key()
public_key_b = key_b.public_key()

m = "The name of our country is Bangladesh"
print(f"The message is : {m}\n")
hashed = SHA1.new(m.encode())
print(f"The hashed message: {b64(hashed.digest())}\n")
signature = pkcs1_15.new(private_key_a).sign(hashed)
print(f"The signature is: {b64(signature)}\n")
packet1 = signature+m.encode()
print(f"The packet1: {b64(packet1)}\n")

zipped = zlib.compress(packet1)
print(f"The zipped file: {b64(zipped)}\n")

ks = get_random_bytes(16)
iv = get_random_bytes(16)
aes = AES.new(ks, AES.MODE_CBC, iv)
encrypted_message = aes.encrypt(pad(zipped, 16))
encrypted_key = PKCS1_OAEP.new(public_key_b).encrypt(ks)
packet2 = encrypted_key+iv+encrypted_message
print(f"Encryted_Message is: {b64(encrypted_message)}\n")
print(f"Encrypted_Key is: {b64(encrypted_key)}\n")
print(f"Packet2 is: {b64(packet2)}\n")
#Store the message
with open("pgp.txt", "wb")as f:
    f.write(packet2)

#Load from file
with open("pgp.txt", "rb")as f:
    packet2 = f.read()


encrypted_key = packet2[:256]
iv = packet2[256:272]
encrypted_message = packet2[272:]

ks = PKCS1_OAEP.new(private_key_b).decrypt(encrypted_key)
print(f"The secret_key is: {b64(ks)}\n")

aes = AES.new(ks, AES.MODE_CBC, iv)
zipped = aes.decrypt(encrypted_message)
zipped = unpad(zipped, 16)

print(f"Zipped message: {b64(zipped)}\n")
unzipped = zlib.decompress(zipped)
print(f"Unzipped message is : {b64(unzipped)}\n")

signature = unzipped[:256]
message = unzipped[256:]

print(f"The message is: {message.decode()}\n")
print(f"The Signature is: {b64(signature)}\n")

hashed_message = SHA1.new(message)

try:
    pkcs1_15.new(public_key_a).verify(hashed_message, signature)
    print("The message is authenticated")
except(ValueError, TypeError):
    print("The message authentication is failed")
