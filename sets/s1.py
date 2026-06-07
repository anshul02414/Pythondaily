s = {1,2,3,4,5}
print(s)
print(type(s))

s2 = set()
print(type(s2))

i = 0
while(i <= 5):
    inp = int(input("Enter the set : "))
    s2.add(inp)
    i += 1

print(s2)
print(len(s2))

# clc len
ln = 0
for i in s2:
    ln+=1

print(ln)

