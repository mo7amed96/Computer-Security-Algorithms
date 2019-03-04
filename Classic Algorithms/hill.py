from textwrap import wrap
from math import sqrt


key_length = int(input())
key_dim = int(sqrt(key_length))
keystr = (input()).split(' ')
plaintxt = input()
key = []

for i in range(key_dim):
    key.append([])
    for j in range (key_dim):
        key[i].append(int(keystr.pop(0)))

while (len(plaintxt) % key_dim) != 0:
    plaintxt = plaintxt + 'X'

plaintxt = wrap(plaintxt,key_dim)
ciphertxt = ''

for block in plaintxt:
    plain_mat=[]
    
    for i in range (key_dim):
        plain_mat.append([])
        plain_mat[i].append( ord(block[i]) - ord('A'))

    for i in range(key_dim):
        cipher_char=0
        for j in range(key_dim):
            temp1=key[i][j]
            temp2=plain_mat[j][0]
            cipher_char += key[i][j] * plain_mat[j][0]
        cipher_char = cipher_char % 26
        ciphertxt = ciphertxt + chr(cipher_char + ord('A'))
    
print(ciphertxt)
