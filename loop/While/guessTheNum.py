import random as rand
num = rand.randint(1, 100)

# guess logic
while True:
    guss = int(input("Enter the number : "))
    if(guss == num):
        print("Got it")
        break
    print("Try Again")