l = [[1,2],[3,4],[5,6]]

newL = []

for i in range(len(l)):
    for j in range(len(l[i])):
        newL.append(l[i][j])
    
print(newL)