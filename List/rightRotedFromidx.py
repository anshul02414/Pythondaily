l = [1,5,9,22,1,6,4,55,6,78,32,4,90,10,55]

idx = int(input(f"Enter The index in range 0 - {len(l)-1} : "))

if idx < 0 or idx >= len(l):
    print("Enter the valid index")
else:
    for i in range(0, idx):
        temp = l.pop()
        l.insert(0,temp)

print(l)