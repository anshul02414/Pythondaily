l = [1,5,9,22,1,6,4,55,6,78,32,4,90,10,55]

traversed = []

for i in range(0,len(l)):
    frq = 0
    
    if(l[i] in traversed):
        continue
    
    for j in range(0, len(l)):
        if l[i] == l[j]:
            frq+=1
    
    traversed.append(l[i])
    
    if frq == 1:
        print(l[i])