st = input("Enter the string : ")

duplicate = ""

for i in range(0, len(st)):
    for j in range(i+1, len(st)):
        if st[i] in duplicate:
            break
        if st[i] == st[j]:
            duplicate += st[i]

print(duplicate)

