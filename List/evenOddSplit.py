l = [1,5,9,22,1,6,4,55,6,78,32,4,90,10,55]

evenL = []
oddL = []

for i in l:
    if i % 2 == 0:
        evenL.append(i)
    else:
        
        oddL.append(i)

print(evenL)
print(oddL)