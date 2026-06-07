l = [5,2,8,8,1,9,9,4]

l = set(l)

largest = float('-inf')
secL = float('-inf')

for i in l:
    if largest < i:
        secL = largest
        largest = i
    
    elif i > secL and i < largest:
        secL = i

print(secL)