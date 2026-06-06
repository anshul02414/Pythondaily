l = [13, 12, 7, 10]

m = 1
for i in l:
    m *= i

print(m)

# print(min(l))
# print(max(l))

minn = l[0]
maxx = l[0]

for i in l:
    if i > maxx:
        maxx = i
    
    if i < minn:
        minn = i
        
print(minn, maxx)