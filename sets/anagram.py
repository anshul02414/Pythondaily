a = "listen"
b = "silent"

if set(a) == set(b):
    print("Anagram hai")
else:
    print("Anagram nhi hai")
    

s1 = "python"
s2 = "typhoon"
print(set(s1).intersection(set(s2)))