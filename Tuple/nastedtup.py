t = ((1, 2), (3, 4), (5, 6))

newt = []

for i in range(len(t)):
    for j in range(len(t[i])):
        newt.append(t[i][j])

newt = tuple(newt)
print(newt)