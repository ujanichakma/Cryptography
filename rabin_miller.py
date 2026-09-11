import random
def miller_robin(p,k):

    if(p<2): return False
    elif(p<=3): return True
    elif(p%2==0): return False
    else:
        m = p-1
        b = 0
        while(m%2==0):
            m//=2
            b+=1
        for _ in range(k):
            a = random.randint(2, p-2)
            z = pow(a,m,p)
            if z==1 or z == p-1:
                continue
            for _ in range(b):
                z = pow(z,2,p)
                if(z==p-1):
                    break
            else:
                return False
        return True

p = 99999999999999999989
k = 10

is_prime = miller_robin(p,k)
if is_prime:
    print("Probably prime")
else:
    print("Definitely composite")
