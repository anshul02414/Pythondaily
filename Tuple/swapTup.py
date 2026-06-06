t = (5,8,3,2,9,1,2,7,8,5,3)

temp = t[0]
t = list(t)
t[0] = t[len(t)-1]
t[len(t)-1] = temp
t = tuple(t)

print(t)