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

print(getpos(14))
print(getindex((2,4)))