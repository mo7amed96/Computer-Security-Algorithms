inputsize = int(input())
permutationvalues = input().split()
inversevalues =[]
irreversible = False
for i in range(inputsize):
    if str((i+1)) in permutationvalues:
        idx = permutationvalues.index(str(i+1))
        inversevalues.append(str(idx+1))
    else:
        irreversible = True
        break
if irreversible:
    print("IMPOSSIBLE")
else:
    print(' '.join(inversevalues))