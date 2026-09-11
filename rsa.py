import math


def get_code():
    p = 97
    q = 89
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while(math.gcd(e, phi)!=1):
        e+=1
    d = pow(e,-1, phi)
    public_key = (e,n)
    private_key = (d,n)

    return public_key, private_key

def encryption(m, key):
    e,n = key
    c = []
    blocks = [
        int(m[i:i+3])
        for i in range(0, len(m), 3)
    ]
    for m in blocks:
        c.append(pow(m,e,n))
    return c
def decryption(cipher,key):
    d,n = key
    m = ""
    for c in cipher:
        m+=str(pow(c,d,n))
    return m

def merge(cipher):
    m = ""
    for c in cipher:
        m+=str(c)
    return m

m = "63636363"
public_key, private_key = get_code()

cipher_text = encryption(m, public_key)
decrypted_text = decryption(cipher_text, private_key)

c = merge(cipher_text)

print(m)
print(c)
print(decrypted_text)
