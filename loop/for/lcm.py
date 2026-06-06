n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the Second Number : "))

a = n1
b = n2

while b != 0:
    a, b = b, a % b

gcd = a

# Find LCM
lcm = (n1 * n2) // gcd

print("LCM =", lcm)