hindi = int(input("Enter the marks of the Hindi : "))
english = int(input("Enter the marks of the English : "))
Math1 = int(input("Enter the marks of the maths : "))

# check the result
persent = (hindi + english + Math1) / 3

if(persent >= 33):
    if (hindi > 33 and english > 33 and Math1 > 33):
        print("Pass")
        # clc grads
        if persent >= 90:
            print("A+")
        elif persent < 90 and persent >= 75:
            print("A")
        elif persent < 75 and persent >= 50:
            print("B")
        elif persent < 50 and persent > 33:
            print("c")
    else:
        print("Fail") 
        print("F")       
else:
    print("Fail")
    print("F")
