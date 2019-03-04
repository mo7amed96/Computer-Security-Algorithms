from textwrap import wrap
import itertools

def getpos(i):
    if i < 5:
        return (0,i)
    elif i<10:
        return (1,i-5)
    elif i<15:
        return (2,i-10)
    elif i<20:
        return (3,i-15)
    elif i<25:
        return(4,i-20)

def getindex(i):
    return i[0]*5+i[1]
 
keyWord = input()
plaintxt = input()
keyWord = keyWord.replace('J','I')
plaintxt = plaintxt.replace('J','I')
keytemp = keyWord
alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
key = []
for c in keyWord:
    if c not in key:
        key.append(c)


for c in alpha :
    if c not in key:
        key.append(c)
key =''.join(key)
key=wrap(key,5)
    
plaintxt = wrap(plaintxt,2) 

plainLength=len(plaintxt)
k=0

while k != plainLength:
    block=plaintxt[k]
    if len(block) <2:
        break
    if block[0] == block[1]:
        if block[0] == 'X':
            block = block[0:1] + 'Q' + block[1:]
        else:
            block = block[0:1] + 'X' + block[1:]
    if len(block) > 2:
        if k == (len(plaintxt) -1):
            plaintxt.append('')
            plainLength = plainLength+1
        plaintxt[k+1] = block[2:] + plaintxt[k+1]
        block = block[0:2]

        
    plaintxt[k]=block
    k = k+1
plaintxt = ''.join(plaintxt)
if (len(plaintxt) % 2) != 0:
    if plaintxt[len(plaintxt)-1] != 'X':
        plaintxt = plaintxt + 'X'
    else:
        plaintxt = plaintxt + 'Q'
plaintxt = wrap(plaintxt,2)
key = ''.join(key)
key = list(key)
ciphertxt=[]
for block in plaintxt:
    
    pos1 = getpos(key.index(block[0]))
    pos2 = getpos(key.index(block[1]))
    
    if pos1[0] == pos2[0]:
        pos1 = (pos1[0],(pos1[1]+1)%5)
        pos2 = (pos2[0],(pos2[1]+1)%5)
    
    elif pos1[1] == pos2[1]:
        pos1 = ((pos1[0]+1)%5,pos1[1])
        pos2 = ((pos2[0]+1)%5,pos2[1])
    
    else:
        temp=pos1
        pos1 = (pos1[0],pos2[1])
        pos2 = (pos2[0],temp[1])
    
    ciphertxt.append(key[getindex(pos1)])
    ciphertxt.append(key[getindex(pos2)])

ciphertxt = ''.join(ciphertxt)
print(ciphertxt)
    
        
    