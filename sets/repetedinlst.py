l = [5,3,1,4,3,2,1]

s = set()

for i in l:
    if i in s:
        print(i)
        break
    s.add(i)
    