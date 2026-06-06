l = [1,5,9,22,6,78,32,4,90,10,55]
print(l)

for j in range(0, len(l)):
    for i in range(j+1, len(l)):
        if l[j] > l[i]:
            # swap
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)