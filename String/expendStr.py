st = input("Enter the string : ")

# Compressed String 
newSt = ""

for i in range(0, len(st), 2):
    n = st[i] * int(st[i+1])
    newSt += n

print(newSt)