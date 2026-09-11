import hashlib
def md5(text):
    hashed = hashlib.md5(text.encode())
    return hashed.hexdigest()


text = "The name of my country is Bangledesh"
hashed = md5(text)
print(hashed)
