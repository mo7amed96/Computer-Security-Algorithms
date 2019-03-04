from textwrap import wrap
import itertools as it

def getpos(i):
    if i < 3:
        return (0,i)
    elif i<6:
        return (1,i-3)
    elif i<9:
        return (2,i-6)

def getindex(i):
    return i[0]*3+i[1]

def playfair(keyWord,plaintxt):
    alpha = 'ABCDEFGHI'
    key = []
    for c in keyWord:
        if c not in key:
            key.append(c)
    
    
    for c in alpha :
        if c not in key:
            key.append(c)
    key =''.join(key)
   # key=wrap(key,3)
        
    plaintxt = wrap(plaintxt,2) 
    
   # key = ''.join(key)
    key = list(key)
    ciphertxt=[]
    for block in plaintxt:
        
        pos1 = getpos(key.index(block[0]))
        pos2 = getpos(key.index(block[1]))
        
        if pos1[0] == pos2[0]:
            pos1 = (pos1[0],(pos1[1]+1)%3)
            pos2 = (pos2[0],(pos2[1]+1)%3)
        
        elif pos1[1] == pos2[1]:
            pos1 = ((pos1[0]+1)%3,pos1[1])
            pos2 = ((pos2[0]+1)%3,pos2[1])
        
        else:
            temp=pos1
            pos1 = (pos1[0],pos2[1])
            pos2 = (pos2[0],temp[1])
        
        ciphertxt.append(key[getindex(pos1)])
        ciphertxt.append(key[getindex(pos2)])
    
    ciphertxt = ''.join(ciphertxt)
    return ciphertxt

alpha = 'ABCDEFGHI'
alpha = list(alpha)
plaintxt=input()
ciphertxt = input()
keysComb = list(it.permutations(alpha, 9))
for keyComb in keysComb:
    if ciphertxt == playfair(''.join(keyComb),plaintxt):
        print(''.join(keyComb))
        break

    
        
    