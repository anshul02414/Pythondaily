nums = [1,5,3,4,2]
k = 2
s = set()

for i in nums:
    if i-k in s:
        print(i-k, i)
        s.add(i)
        break
    s.add(i)