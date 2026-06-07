nums = [2,7,11,15,3,6]
target = 9
s = set()

for i in nums:
    if target-i in s:
        print(target-i,i)
        break
    s.add(i)
