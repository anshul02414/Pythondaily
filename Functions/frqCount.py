def frequency(lst, el):
    f = 0
    for i in lst:
        if i == el:
            f += 1
    return f


print(frequency([1,2,2,3,2], 2))