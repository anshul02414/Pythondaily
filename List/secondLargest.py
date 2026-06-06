# l = [1,5,9,22,6,78,32,4,90,10,55]

# # 2nd largest
# l.remove(max(l))
# print(max(l))

# # 2nd smallest
# l.remove(min(l))
# print(min(l))


l = [1,5,9,22,6,78,32,4,90,10,55]

largest = l[0]
secLarg = l[0]

for i in range(0, len(l)):
    if l[i] > largest:
        temp = largest
        largest = l[i]
        secLarg = temp
        
print(secLarg)