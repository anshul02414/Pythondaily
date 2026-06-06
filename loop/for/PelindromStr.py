st = str(input("Enter the String : "))
rev = ""

for i in range (len(st)-1, -1, -1):
    rev += st[i]

if st == rev:
    print("Pelindron Str")
else:
    print("Not pelindrom String")
    

    