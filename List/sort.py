l = [1,5,9,22,1,6,4,55,6,78,32,4,90,10,55]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]:
            # swap
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)