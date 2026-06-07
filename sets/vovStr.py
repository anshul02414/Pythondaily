s = "programming"

st = set()

for i in s.lower():
    if i in "aeiou":
        st.add(i)
print(st)

A = {1,2,3,4,5,6,7,8,9}
B = {2,4,6,8}

print(A-B)