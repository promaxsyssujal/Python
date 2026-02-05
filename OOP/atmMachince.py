class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        while True:
            user_input=input("""
Enter your Choice
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to Check Balance
5. Enter 5 to exit
""" )

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin=input("Create your Pin")
        print("Pin is created")

    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter your amount to deposit"))
            self.balance=self.balance+amount
            print("Amount is deposited")
        else:
            print("Pin is invalid")    

    def withdraw(self):
        temp=input("Enter your pin")  
        if temp==self.pin:
            amount=int(input("Enter amount for withdraw"))
            self.balance=self.balance-amount
            print("Amount is withdrawl")
        else:
            print("Pin is invalid")    

    def check_balance(self):
        temp=input("Enter Your Pin")
        if temp==self.pin:
            print("Balance>>",self.balance)
        else:
            print("Pin is invalid")    
 


atm=Atm()