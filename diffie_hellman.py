import random
def get_premitive_root(q):
    for a in range(2,q):
        flag = True
        for i in range(1, q-1):
            x = pow(a,i,q)
            if x==1:
                flag = False
                break
        if flag==True:
            return a
def diffie_hellman(q,a):
    xa, xb = random.randint(2, q-2), random.randint(2,q-2)
    print(f"Private key of Alic is: {xa}\n Private key of Bob is: {xb}")
    ya, yb = pow(a, xa,q), pow(a,xb,q)
    print(f"Public key of Alic is: {ya}\n Public key of Bob is: {yb}")
    print("After Exchanging the public keys")
    sa, sb = pow(yb,xa,q), pow(ya,xb,q)
    if(sa==sb):
        print(f"They got similar secret key\n And the key is: {sa}")
    else:
        print("They did not get the similar secret key")

q = 23
a = get_premitive_root(q)
print(f"The premitiva root of {q} is : {a}")
diffie_hellman(q,a)
