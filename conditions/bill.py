unit = int(input("Enter the units of the Electricty : "))

if unit < 0:
    print("Invalid Units!!")
else:
    if(unit >= 0 and unit <= 100):
        print("Bill = ", unit * 5)
    elif (unit > 100 and unit <= 200):
        print("Bill = ", unit*7)
    else:
        print("Bill = ", unit*10)