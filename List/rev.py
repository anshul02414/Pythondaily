l = [4,5,7,2,4,7]

# l.reverse()
print(l)

new = []

for i in range(len(l) - 1, -1, -1):
    new.append(l[i])
    
print(new)