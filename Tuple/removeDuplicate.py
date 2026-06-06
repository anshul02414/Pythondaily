t = (5,8,3,2,9,1,2,7,8,5,3)

newl = []

for i in t:
    if i not in newl:
        newl.append(i)

print(newl)
newl = tuple(newl)
print(newl)