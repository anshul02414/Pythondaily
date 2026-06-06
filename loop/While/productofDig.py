n = int(input("Enter the number : "))

Product = 1

while n > 0:
    Product = Product * (n % 10)
    n = n // 10

print(Product)
