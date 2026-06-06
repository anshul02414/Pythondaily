t = (5,8,3,2,9,1,2,7,8,5,3)

min = t[0]
max = t[0]

for i in t:
    if min > i:
        min = i
    if max < i:
        max = i
    
print(min)
print(max)