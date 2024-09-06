class Bank_Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount !")
        else:
            self.balance += amount
            print(f"Your amount of {amount} is deposited ")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount !")
        elif self.balance < amount:
            print("Insufficient funds !")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Your amount of {amount} is withdrawn ")

    def check_balance(self):
        print(f"Your balance is {self.balance}")


obj = Bank_Account()

while True:

    print("-----------------------")
    print("1. Deposit ")
    print("2. Withdraw ")
    print("3. Check Balance")
    print("4. Exit")
    print("-----------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        obj.deposit(int(input("Enter Amount: ")))
    elif choice == "2":
        obj.withdraw(int(input("Enter Amount: ")))
    elif choice == "3":
        obj.check_balance()
    elif choice == "4":
        print("Exiting.....")
        break
