s = {1,2,3,4,5}
print(s)
print(type(s))

el = int(input("Enter the el : "))
s.add(el)
print(s)

print(5 in s)
print(88 in s)

s.remove(5)
print(s)

s.clear()

print(s, type(s))