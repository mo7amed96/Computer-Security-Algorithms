outputsize = int(input())
permutationValues = (input()).split()
inputsize = int(input())
inputvalue = input()
inputvalue =list(bin((int(inputvalue,16)))[2:])

if (len(inputvalue) < inputsize):
    temp = inputsize - len(inputvalue)
    temp = ['0'] * temp
    inputvalue = temp + inputvalue


outputvalue =[]

for i in permutationValues:
    temp = int(i)
    outputvalue.append(inputvalue[temp-1])

outputvalue = ''.join(outputvalue)
outputvalue = format(int(outputvalue,2),'02x')
outputvalue = outputvalue.upper()
print(outputvalue)
