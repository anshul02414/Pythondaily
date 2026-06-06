# check frequency of every chr in str
st = str(input("Enter The String : "))
visited = ""

for i in st:
    if i not in visited:
        count = 0
        for j in st:
            if i == j:
                count += 1
                
        print(i, " : ", count)
        visited += i
