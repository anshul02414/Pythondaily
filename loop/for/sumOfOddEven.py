sumOdd = 0
sumEven = 0

for i in range(1, 51):
    if(i % 2 == 0):
        sumEven += i 
    else:
        sumOdd += i

print("Odd = ", sumOdd)
print("Even = ", sumEven)