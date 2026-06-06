num = 29

print(bin(num))

b = ""

while num > 0:
    if(num % 2 == 0):
        b += '0'
    else:
        b += '1'
    num //= 2

print(b[::-1])