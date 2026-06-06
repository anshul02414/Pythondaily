import math

n = int(input("Enter the number : "))

n1 = n
strong = 0

while n > 0:
    strong += math.factorial(n%10)
    n //= 10

if(n1 == strong):
    print("Yes Strong")
else:
    print("Not")