balance = 10000
print("Choose from the following : ")
choice = int(input("1. Deposite\n2. Withdraw\n3. Bal inquiry\n4. Exit\n"))

if choice == 1:
    depo = int(input("Enter the amount : "))
    print(f"Balance : {balance + depo}\n")

elif choice == 2:
    withdraw = int(input("Enter the amount : "))
    if(balance - withdraw > 100):
        print(f"Balance : {balance - withdraw}\n")
    elif balance - withdraw < 100:
        print("Cannot withdraw! Balance have to be at least 100$!")

elif choice == 3:
    print(f"Balance : {balance}\n")

elif choice == 4:
    print("Thanks for using our bank! Have a nice day!")
else:
    print("Wrong choice!")