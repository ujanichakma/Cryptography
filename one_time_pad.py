def encryption(text):
    size = len(text)
    with open("5.one_time_pad.txt","r") as f:
        key = f.read().strip()[:size]
    result = ""
    for p, k in zip(text, key):
        if p==" ":
            result+=p
        else:
            if p.isupper():
                p = ord(p)-65
                k = ord(k)-65
                c = (p+k)%26
                result+=chr(c+65)
            else:
                p = ord(p)-97
                k = ord(k)-65
                c = (p+k)%26
                result+=chr(c+97)
    return result

def decryption(cipher):
    size = len(cipher)
    with open("5.one_time_pad.txt","r") as f:
        key = f.read().strip()[:size]
    result = ""
    for p, k in zip(cipher, key):
        if p==" ":
            result+=p
        else:
            if p.isupper():
                p = ord(p)-65
                k = ord(k)-65
                c = (p-k)%26
                result+=chr(c+65)
            else:
                p = ord(p)-97
                k = ord(k)-65
                c = (p-k)%26
                result+=chr(c+97)
    return result

text = "Thz name of my country is Bangladesh"
c = encryption(text)
p = decryption(c)
print(text)
print(c)
print(p)
