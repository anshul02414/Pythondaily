l = [1,2,3,2,1]

l1 = l[::-1]
pelindrom1 = True

for i, j in zip(l, l1):
    if i != j:
        pelindrom1 = False

print(pelindrom1)