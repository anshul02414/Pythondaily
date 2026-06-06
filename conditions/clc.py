print("Choice : + - * / \n")
choice = str(input("enter the choice : "))

a = int(input("Enter the a : "))
b = int(input("Enter the b : "))

if(choice == '+'):
    print(a + b)
elif choice == '-':
    print(a - b)
elif choice == '*':
    print(a * b)
elif choice == '/':
    print(a / b)
else:
    print("Invalid Entry!!")
    
