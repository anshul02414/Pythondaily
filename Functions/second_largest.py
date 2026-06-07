def secLarg(list):
    larg = float('-inf')
    seclrg = float('-inf')
    
    for i in list:
        if larg < i:
            secLarg = larg
            larg = i
        
        elif i > secLarg and i < larg:
            secLarg = i
    
    return secLarg

print(secLarg([1,8,6,4,7,9]))