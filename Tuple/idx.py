t = (5,8,3,2,9,1,2,7,8,5,3)

el = int(input("Enter the element : "))
idx = 0

for i in t:
    if i == el:
        print(idx)
    idx+=1