t = tuple()

print(type(t))

tup = (1,2,3,4,5,6,7,8,9,10)
print(tup)
print(type(tup))
print(len(tup))
print(tup.count(6))
print(tup.index(6))

el = int(input("Enter the data : "))

if el in tup:
    print("Data in tup")
else:
    print("Data not in Tup")