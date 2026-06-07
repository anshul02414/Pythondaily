def fibonaccied(n):
    l = []
    a = 0
    b = 1
    for i in range(n):
        l.append(a)
        temp = b
        b = a
        a = temp + b
    return l

print(fibonaccied(7))