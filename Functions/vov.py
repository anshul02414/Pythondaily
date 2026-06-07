def vovels(str):
    v = 0
    for i in str.lower():
        if i in "aeiou":
            v+=1
    return v

print(vovels("Hello"))