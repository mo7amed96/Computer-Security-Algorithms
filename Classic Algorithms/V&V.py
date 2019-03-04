key = input()
plaintxt = input()
oneTimePad = (len(key) == len(plaintxt))
one = 'YES'
if not oneTimePad:
    lendiff = len(plaintxt) - len(key)
    while lendiff > len(key):
        lendiff = lendiff - len(key)
        key=key+key
    key = key + key[0:lendiff]
    one = 'NO'

Vigenere = ''
Vernam = ''

for i in range(len(plaintxt)):
    p1 = ord(plaintxt[i]) - ord('A')
    k1 = ord(key[i]) - ord('A')
    Vigenere = Vigenere + chr(((p1+k1)%26) + ord('A'))
    Vernam = Vernam + format((ord(plaintxt[i]) ^ ord(key[i])),'02x')

print('Vigenere: '+Vigenere)
print('Vernam: '+Vernam.upper())
print('One-Time Pad: '+one)