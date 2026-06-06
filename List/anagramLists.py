l1 = [1, 2, 2, 3]
l2 = [2, 3, 1, 2]

l1.sort()
l2.sort()

if l1 == l2:
    print("Anagram")
else:
    print("Not Anagram")