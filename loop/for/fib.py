a = 0
b = 1
length = int(input("Enter the length of the Series : "))

for i in range(length):
    print(a, end=" ")
    next = a + b
    a = b
    b = next
    

