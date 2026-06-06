num = int(input("Enter the Number : "))

# check the digit
num = str(num)

if len(num) == 1:
    print("Single Digit")
elif len(num) == 2:
    print("Two digits")
elif len(num) == 3:
    print("3 digits")
elif len(num) == 4:
    print("4 digits")
else:
    print("Kun batau!!")
