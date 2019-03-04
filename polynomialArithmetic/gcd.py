def gcd(a,b):
    
    while b != 0:
        temp = a % b
        a=b
        b=temp
    return a

values = input().split()
print(gcd(int(values[0]),int(values[1])))
