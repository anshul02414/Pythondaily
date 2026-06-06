st = input("Enter the string : ")

new = ""

for i in range(0, len(st)):
    if st[i] not in new:
        new += st[i]

print(new)