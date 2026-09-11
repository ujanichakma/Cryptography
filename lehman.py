import random
def isPrime(p,k):
    if(p<2):return False
    elif(p<=3):return True
    elif(p%2==0):return False
    else:
        for i in range(k):
            a = random.randint(2, p-2)
            r = pow(a,(p-1)//2,p)
            if r!=1 and r!=p-1:
                return False
        return True


p = 99999999999999999989
k=5
if(isPrime(p,k)):
    print("Probably prime")
else:
    print("Definitely not prime")
