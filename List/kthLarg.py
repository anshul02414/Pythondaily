l1 = [1,5,9,22,6,78,32,4,90,10,55]

l1.sort()
print(l1)

idx = int(input("Enter the index for kth largest : "))

for i in range(idx-1):
    l1.pop()

print(l1[len(l1)-1])