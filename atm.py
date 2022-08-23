import random
import sys

class ATM():
    def __init__(self, name, account_number,pin=None, balance = 0):
        self.name = name
        self.account_number = account_number
        self.pin=pin
        self.balance = balance

         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")

    def case_note(self,amount):
        try:
            note2000=0
            note500=0
            note200=0
            note100=0
            note50=0
            while(amount!=0):
                
            
                if amount >= 2000:
                    note2000 = amount//2000
                    amount -= note2000 * 2000
                    
                elif amount >= 500:
                    note500 = amount//500
                    amount -= note500 * 500
                 
                elif amount >= 200:
                    note200 = amount//200
                    amount -= note200 * 200
                   
                elif amount >= 100:
                    note100 = amount//100
                    amount -= note100 * 100
                     
                elif amount >= 50:
                    note50 = amount//50
                    amount -= note50 * 50
            print(f'Notes AVAILABLE IN Machine \n2000 : {note2000}\n 500 : {note500}\n 200 : {note200}\n 100 : {note100}\n 50  : {note50}\n')

        except:
                print("Not Found")
         
    def deposit(self, amount):
        self.amount = amount
        pin_check=int(input('Enter your Pin :'))
        if int(pin)==pin_check:
            self.balance = self.balance + self.amount
            atm.case_note(self.balance)
                       
            print()
        else:
            print('Enter The valid Pin')
            self.balance = self.balance 
            
 
    def withdraw(self, amount):
        self.amount = amount
        pin_check=int(input('Enter your Pin :'))
        if int(pin)==pin_check:
            if self.amount > self.balance:
                print("Insufficient fund!")
                print(f"Your balance is Nu.{self.balance} only.")
                print("Try with lesser amount than balance.")
                print()
            else:
                self.balance = self.balance - self.amount
                print(f"Nu.{amount} withdrawal successful!")
                print("Current account balance: Nu.", self.balance)
                atm.case_note(self.balance)
                print()
        else:
            print('Enter The valid Pin')
            self.balance = self.balance 
 
    def check_balance(self):
        pin_check=int(input('Enter your Pin :'))
        if int(pin)==pin_check:
            print("Available balance: Nu.", self.balance)
            print()
        else:
            print('Enter The valid Pin')
            self.balance = self.balance
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            0. Case Note Available
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                print("""
            TRANSACTION 
        *********************
            Menu:
            0. Case Note Available
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option==0:
                    atm.case_note(amount=0)
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                    
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    sys.exit()
                 
 
print("*******WELCOME TO BANK OF Haidar*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
pin = input("set your pin: ")

print("Congratulations! Account created successfully......\n")
 
atm = ATM(name, account_number,pin)
 
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
    
