l = [4,5,7,2,4,7,66,34,54,65,676]

od = 0
ev = 0

for i in l:
    if i % 2 == 0:
        ev += 1
    else:
        od += 1

print("Odd ", od)
print("Even ",ev)
print(len(l))