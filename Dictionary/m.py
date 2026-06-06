d = {
    "a": 2,
    "b": 3,
    "c": 4,
    "d": 5
}

re = 1

for i in d.values():
    re *= i

print(re)