def count_upper(str):
    up = 0
    for i in str:
        if i == i.upper():
            up += 1
    return up

print(count_upper("PyThOn"))