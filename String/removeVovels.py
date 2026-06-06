st = input("Enter the string : ")

new = ""
vovels = "AEIOUaeiou"

for i in range(0, len(st)):
    if(st[i] not in vovels):
        new += st[i]

print(new)