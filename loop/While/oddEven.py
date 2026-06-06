i = 1
odd = 0
even = 0

while(i <= 50):
    if(i % 2 == 0):
        even += i
    else:
        odd += i
    i += 1

print("odd : ", odd)
print("Even : ", even)