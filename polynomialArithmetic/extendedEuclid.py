def gcd(a,b):
    
    while b != 0:
        temp = a % b
        a=b
        b=temp
    return a

def extendedEuclid(m,b):
    (A1,A2,A3) = (1,0,m)
    (B1,B2,B3) = (0,1,b)
    while(True):
        if B3 == 0:
            return -1
        elif B3 == 1:
            return B2%m
        else:
            Q = int (A3/B3)
            (T1,T2,T3) = (A1-Q*B1,A2-Q*B2,A3-Q*B3)
            (A1,A2,A3) = (B1,B2,B3)
            (B1,B2,B3) = (T1,T2,T3)
        

values = input().split()
mulinverse = extendedEuclid(int(values[0]),int(values[1]))
addinverse = (int(values[0]) - int(values[1])) % int(values[0])

if mulinverse == -1:
    print("IMPOSSIBLE")
else:
    print(addinverse,mulinverse)