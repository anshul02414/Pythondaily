hindi = int(input("Enter the marks of the Hindi : "))
english = int(input("Enter the marks of the English : "))
Math1 = int(input("Enter the marks of the maths : "))

# check the result
persent = (hindi + english + Math1) / 3

if(persent >= 33):
    if (hindi > 33 and english > 33 and Math1 > 33):
        print("Pass")
    else:
        print("Fail")        
else:
    print("Fail")
