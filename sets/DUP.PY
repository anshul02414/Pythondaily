# l = [2,4,552,1,5,2,1,4,34,5]
l = [5,2,8,8,1,9,9,4]

seen = set()
duplicate = set()

for i in l:
    if i in seen :
        duplicate.add(i)
    else:
        seen.add(i)

print(duplicate)