# consonant vovel digit

consonants = "bcdfghjklmnpqrstvwxyz"
vvels = "aeiou"
dig = "123456789"

inp = str(input("Enter the digit : "))

inp = inp.lower()

# check dig
if(inp in consonants):
    print(f"{inp} is Consonant")
elif(inp in vvels):
    print(f"{inp} is Vovels")
elif(inp in dig):
    print(f"{inp} is Number")
else:
    print(f"{inp} is Special Charecter")