w = input("Enter The Word : ")

l = w.split(' ')
longest = l[0]


for i in l:
    # print(i)
    if len(i) >= len(longest):
        longest = i



print(longest)