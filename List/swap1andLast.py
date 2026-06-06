l = ["Apple", "Banana", "Mango", "StrawBerry"]
print(l)
# swap

temp = l[0]
l[0] = l[3]
l[3] = temp

print(l)

# add new at 2nd pops
l[1] = "Koi naya fruit"
print(l)

# delet 3rd
l.pop(2)

print(l)