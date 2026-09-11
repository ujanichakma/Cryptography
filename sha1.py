import hashlib
def sha(text):
    hashed = hashlib.sha1(text.encode())
    return hashed.hexdigest()


text = "The name of my country is Bangledesh"
hashed = sha(text)
print(hashed)

     
