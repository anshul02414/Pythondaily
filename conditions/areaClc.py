import math

# area calculator
print("""Area Calculator\n
      1 -> for circuler\n
      2 -> for ractanguler\n
      3 -> for squre\n""")

choice = int(input("Enter your choice: (1-4) : "))

if choice == 1:
    print("Area of the circle")
    r = float(input("Enter the redius of the circle : "))
    # area clc
    area = math.pi * (r ** 2)
    print(f"Area of Circle with {r} : {area:.3f}")
elif choice == 2:
    print("Area of the ractanguler")
    a = float(input("Enter tha Height : "))
    b = float(input("Enter the Bridth : "))
    area = a * b
    print(f"Area of the ractanguler with h : {a} w : {b} = {area}")
elif choice == 3:
    print("Area of the Squre: ")
    a = float(input("Enter the width of the Squre : "))
    area = a ** 2
    print(f"Area of the Squre with width : {a} = {area}")
else:
    print("Invalid Entry!")
    
