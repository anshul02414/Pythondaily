inp = input("Enter the String : ")

Vovels = "AEIOUaeiou"
vnum = 0
cnum = 0

for i in range(0, len(inp)):
    if inp[i] in Vovels:
        vnum += 1
    else:
        cnum += 1

print(vnum)
print(cnum)