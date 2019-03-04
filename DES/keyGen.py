from textwrap import wrap
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]
Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

def circular_shift(num,value):
    value = value[num:] + value[0:num]
    return value

def perm_choice1(inputvalue):
    global PC1
    inputvalue = list(inputvalue)
    outputvalue =[]
    
    for i in PC1:
        temp = int(i)
        outputvalue.append(inputvalue[temp-1])
    
    outputvalue = ''.join(outputvalue)
    outputvalue = int(outputvalue,2)
    return outputvalue

def perm_choice2(inputvalue):
    global PC2
    inputvalue = list(inputvalue)
    outputvalue =[]
    
    for i in PC2:
        temp = int(i)
        outputvalue.append(inputvalue[temp-1])
    
    outputvalue = ''.join(outputvalue)
    outputvalue = int(outputvalue,2)
    return outputvalue

def key_gen():
    global Rotations,PC2
    key = input()
    keysize = len(key)*4
    key = list(bin((int(key,16)))[2:])
    if len(key) < keysize:
        temp = keysize - len(key)
        temp = ['0']*temp
        key = temp+key
    key = perm_choice1(key)
    
    key = list(bin(key)[2:])
    
    if len(key) < 56:
        temp = 56 - len(key)
        temp = ['0']*temp
        key = temp+key
    key =''.join(key)
    key = wrap(key,28)
    
    output = []
    
    for i in Rotations:
        key[0] = circular_shift(i,key[0])
        key[1] = circular_shift(i,key[1])
        temp = key[0] + key[1]
        output.append(perm_choice2(temp))
        
    for o in output:
       o = format(o,'02x')
       if len(o) < 12:
           o = list(o)
           temp = 12 - len(o)
           temp = ['0'] * temp
           o = temp + o
           o = ''.join(o)
       print(o.upper())

key_gen()
        
    
    
        