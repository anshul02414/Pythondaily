# Count digits, alphabets, and special characters separately.
st = input("Enter the String : ")

st = st.lower()
vovels = "aeiou"
Consonants = "bcdfghjklmnpqrstvwxyz"

v = 0
cons = 0
spCh = 0

for i in st:
    if i in vovels:
        v += 1
    elif i in Consonants:
        cons += 1
    else:
        spCh += 1

print(v,cons,spCh)
        