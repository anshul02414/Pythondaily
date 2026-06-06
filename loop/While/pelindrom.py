n = int(input("Enter the number : "))

n1 = n
rev = 0

while n1 > 0:
    rev = rev * 10 + (n1 % 10)
    n1 = n1 // 10

print(rev)

if(rev == n):
    print("Pelindrom")
else:
    print("Not Pelindrom")
