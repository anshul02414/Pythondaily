d = {
    "apple": 5,
    "banana": 2,
    "mango": 9,
    "grapes": 3,
    "orange": 7
}

# sorted(d) sort by keys

# sort by value
s = sorted(d.items(), key=lambda x: x[1])
print(s)