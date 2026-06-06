name = str(input("Enter the Name of the costumer : "))
NameofP = []
PriceList = []

while True:
    pName = str(input("Enter the nbame of the Product : "))
    NameofP.append(pName)
    quntity = int(input("Enter the Quntity of the Product : "))
    price = int(input("Enter the price of the Product : "))
    PriceList.append(quntity*price)
    
    choice = input("Do you have any more item (yes or no) : ")
    if choice == "no":
        break

j = 0
print("---------------Bill------------")
print("Name of Costumer: ", name)
for i in NameofP:
    print(i,"\t", PriceList[j])
    j = j + 1
Total = 0
for i in PriceList:
    Total += i

print("Total : ", Total)
        