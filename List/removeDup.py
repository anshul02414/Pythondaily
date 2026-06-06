l = [1,2,2,3,4,4,5]
newL = []

for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            break
    if l[i] not in newL:
        newL.append(l[i])

print(l)
print(newL)