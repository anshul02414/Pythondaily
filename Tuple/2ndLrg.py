t = (5,8,3,2,9,1,2,7,8,5,3)

largest = secLargest = float('-inf')

for i in t:
    if i > largest:
        secLargest = largest
        largest = i
    elif largest  > i > secLargest:
        secLargest = i

print(secLargest)