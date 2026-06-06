a = int(input("Enter the num1 : "))
b = int(input("Enter the num2 : "))
c = int(input("Enter the num3 : "))

# check for largest number
if(a > b and a > c):
    print("a large")
elif (b > c and b > a):
    print("b large")
elif(a == b == c):
    print("All equal")
else:
    print("c is large")
    
    