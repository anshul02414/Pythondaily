l1 = [1,2,3,4]
l2 = [3,4,5,6]

comL = []

for i in l1:
    for j in l2:
        if i == j:
            comL.append(i)

print(comL)