s = str(input("Enter the String : "))
new = "" 

for i in range(0, len(s)):
    if s[i] == " ":
        new += "_"
    else:
        new += s[i]

print(new)

print(new.replace("_", "+"))