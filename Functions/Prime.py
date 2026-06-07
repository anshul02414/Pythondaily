import math

def check_Prime(n):
    isp = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            isp = False
            break
    return isp

print(check_Prime(5))
print(check_Prime(8))