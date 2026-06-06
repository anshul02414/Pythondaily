d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}

for key, value in d2.items():
    d1.update({key:value})
    
print(d1)
