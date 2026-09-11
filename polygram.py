with open("blocks.txt", "r") as f:
    data = f.read().split()

def encryption(text):
    result = ""

    for i in range(0, len(text),3):
        block = text[i:i+3]
        for j in range(0, len(data), 2):
            if block==data[j]:
                result+=data[j+1]
                break
    return result
def decryption (cipher_text):
    result = ""
    for i in range(0, len(cipher_text),3):
        block = cipher_text[i:i+3]
        for j in range(0, len(data), 2):
            if block==data[j+1]:
                result+=data[j]
                break
    return result
text = "THENAMEOFOURCOUNTRYISBANGLADESH"
c = encryption(text)
p = decryption(c)
print(c)
print(p)
