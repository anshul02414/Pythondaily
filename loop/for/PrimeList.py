import math

for i in range(2, 101):
    isPrime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            isPrime = False
            break
    
    if isPrime:
        print(i, end=" ")