s = "banana"

output = {}
travelled = ""

# {'b':1, 'a':3, 'n':2}
for i in range(0, len(s)):
    if s[i] in travelled:
        continue
    
    travelled += s[i]
    c = 0
    for j in s:
        if s[i] == j:
            c+=1
    output.update({s[i]:c})

print(output)