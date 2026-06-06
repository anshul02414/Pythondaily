s = str(input("Enter the String : "))

print(True if(s == ''.join(reversed(s))) else False)