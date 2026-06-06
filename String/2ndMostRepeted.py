st = input("Enter the String : ")

tr = ""
mostocc1st = 0
mostocc2nd = mostocc1st

for i in st:
    
    if i in tr:
        continue
    
    c = 0
    for j in st:
        if i == j:
            c += 1
    tr += i
    
    if c > mostocc1st:
        mostocc2nd = mostocc1st
        mostocc1st = c
        
    elif c > mostocc2nd:
        mostocc2nd = c

print(mostocc2nd)