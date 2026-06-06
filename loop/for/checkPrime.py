import math

n = int(input("Enter the number : "))
prime = True

for i in range(2, int(math.sqrt(n)) +1 ):
    if(n % i == 0):
        prime = False
        break

print(prime)