st = input("Enter the String : ")

new = ""

for i in range(0, len(st)):
    if st[i] ==" " and i > 0 and st[i-1] == " ":
        continue
    new += st[i]

print(st)
print(new)
print(len(new))