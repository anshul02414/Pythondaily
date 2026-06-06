l = [1,5,9,22,6,78,32,4,90,10,55]

smallest = l[0]
secSmallest = float('inf')

for i in range(0, len(l)):
    if smallest > l[i]:
        secSmallest = smallest
        smallest = l[i]

    elif l[i] < secSmallest and l[i] != smallest:
        secSmallest = l[i]
        
        
print(smallest)
print(secSmallest)
