l1 = [1,2,3,4]
l2 = [3,4,5,6,4]

newL = l1+l2

union = []

for i in newL:
    for j in newL:
        if i not in union:
            if i == j:
                union.append(i)

print(union)