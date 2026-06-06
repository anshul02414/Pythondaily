l = [1,2,2,3,3,3,2,4,1,7,8,2,4,3,3]

print(len(l))
traversed = []

for i in l:
    f = 0
    if i in traversed:
        continue
    for j in l:
        if i == j:
            f+=1
    traversed.append(i)
    print(i, ": ", f)

