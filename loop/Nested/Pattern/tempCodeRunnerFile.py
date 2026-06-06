for i in range (1, 6):
    for j in range (0, 6):
        if (i <= j):
            print("  ", end="")
        else:
            print("* ", end="")
    print()