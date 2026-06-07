def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > b and c > a:
        return c
    elif a == b == c:
        return "Equal"
    else:
        return "Somthind bad happen"

print(largest(5, 9, 2))