t = (5,8,3,2,9,1,2,7,8,5,3)

re = []

for i in range(len(t)-1, -1, -1):
    re.append(t[i])

re = tuple(re)
print(re)