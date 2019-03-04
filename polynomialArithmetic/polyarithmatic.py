import re
def add (num1,num2):
    num1 = int(num1,16)
    num2 = int(num2,16)
    return format(num1 ^ num2,'02x').upper()

def mulx(num):
    if num < 128:
        num =num << 1
    else:
        num = ((num<<1) ^ (0x1B)) & 0x00FF
    
    return num

def mulxi(num,i):
    
    for k in range(i):
        num = mulx(num)
    return num

values = input().split()

num1 = values[0]
num2 = values[1]
addresult = add(num1,num2)

num1 = int(num1,16)
num2 = int(num2,16)
num2bin = bin(num2)[2:]
while len(num2bin) < 8 :
    num2bin = '0' + num2bin
pos = [x.start() for x in re.finditer('1',num2bin)]
mulresult = 0

for i in pos:
    mulresult ^= mulxi(num1,7-i)

mulresult = format(mulresult,'02x').upper()
print(addresult,mulresult)

