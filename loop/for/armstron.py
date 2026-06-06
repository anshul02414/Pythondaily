n = int(input("Enter the number : "))

n1 = n
arm = 0

while n > 0:
    arm += (n % 10) ** len(str(n1))
    n = n // 10

if n1 == arm:
    print("Armstrong")
else:
    print("Not")