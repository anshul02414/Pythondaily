st = input("Enter the String : ")

for i in range(len(st)):
    for j in range(i+1, len(st)+1):
        print(st[i:j])