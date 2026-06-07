def checkPelindrom(st):
    if st == st[::-1]:
        return True
    else:
        return False


print(checkPelindrom("abcaba"))