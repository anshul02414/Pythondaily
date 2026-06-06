# largest comoun factor

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second Number : "))

gcd = 1
small = n1

if(n1 < n2):
    small == n1
else:
    small = n2

for i in range (2, small+1):
    if(n1 % i == 0 and n2 % i == 0):
        gcd = i

print(gcd)
