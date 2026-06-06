d = {}

for i in range(16):
    d.setdefault(i, i**2)

print(d)