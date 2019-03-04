key = int(input())
plaintxt = input()
ciphertxt = ''
for c in plaintxt:
    
    temp = ord(c) - ord('A')
    temp = (temp + key) % 26
    ciphertxt = ciphertxt + chr(temp+ ord('A'))

print(ciphertxt)