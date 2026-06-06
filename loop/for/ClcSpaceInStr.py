st = str(input("Enter The String : "))

sp = 0

for i in range(0, len(st)):
    if(st[i] == " "):
        sp += 1

print(sp)
