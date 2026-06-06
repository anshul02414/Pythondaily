import time

id = "anshul"
pass1 = "1234ak"

loginState = False

while True:
    for i in range(0, 3):
        idinp = input("Enter the id : ")
        passinp = input("Enter the Password : ")
        if(idinp == id and pass1 == passinp):
            loginState = True
            break
    if(loginState):
        print("LOGING in ....")
        break
    else:
        print("Wait for 10 Seconds!")
        time.sleep(10)

