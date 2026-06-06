l = [1,2,3,5]

for i in range(0, len(l)-1):
    if l[i+1] != l[i]+1:
        print(l[i]+1)
        break
