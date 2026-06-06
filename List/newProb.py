l = [1,0,2,0,3,0,4]
newL = [0] * len(l)
print(newL)

# for i in l:
#     if i == 0:
#         temp = l.remove(i)
#         l.append(temp)

j = 0
for i in range(len(l)):
    if l[i] != 0:
        newL[j] = l[i]
        j+=1

print(newL)
