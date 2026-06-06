s = str(input("Enter the String : "))

vovels = "aeiou"
s = s.lower()
v = 0
l = len(s)

for i in range(0, len(s)):
    if s[i] in vovels: 
        v += 1

print("Consonant = ", l-v)