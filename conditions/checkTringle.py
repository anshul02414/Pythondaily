# check the triangle is valid or not 
h = int(input("Enter the Height of the Tringle : "))
b = int(input("Enter the base of the Tringle : "))
H = int(input("Enter the hypothesis of the Tringle : "))

# check the conditions 
if(h+b) > H:
    print("Posible Triangle")
else:
    print("Not Possible that Tringle")
    