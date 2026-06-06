num = 78

# guess the number
while True:
    inp = int(input("Guess The Number : "))
    if inp == num:
        print("Congrats you got it")
        break
    elif inp < num:
        print("You take less digit")
    else:
        print("Number is very large")

