st = input("Enter the string : ")

travelled = ""

for i in st:
    frq = 0
    if i in travelled:
        continue
    
    for j in st:
        if i == j:
            frq += 1
    print(i, " : ", frq)
    travelled += i