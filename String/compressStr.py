st = input("Enmter the String : ")

newst = ""
travelled = ""

for i in st:
    c = 0
    if i in travelled:
        continue
    
    for j in st:
        if j == i:
            c += 1
    newst += i + str(c)
    travelled += i
    
print(newst)