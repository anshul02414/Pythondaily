A = {1,2,3,4}
B = {3,4,5,6}
c = {4,2,1,3}
d = {1,2,3,4,5,6,7,8}

if A == c:
    print(True)
else:
    print(False)
    
print(A.issubset(d))
print(d.issuperset(A))