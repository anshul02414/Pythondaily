marks = {"a":50, "b":80, "c":70}

max = marks["a"]
min = marks["a"]

for i in marks.values():
    if i > max:
        max = i
    if min > i:
        min = i

print(min)
print(max)