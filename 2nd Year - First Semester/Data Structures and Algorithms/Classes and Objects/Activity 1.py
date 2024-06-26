class BankAccount:

    # M1) Constructor. if no parameters are sent to the __init__ then it initializes account number and balance to 0
    # If there are parameters then it initializes the account number and balance
    def __init__(self, account_number = 0, balance = 0):

        # 1 & 2) Attributes
        self.__account_number = account_number
        self.__balance = balance

    # getter for the account_number
    @property 
    def account_number(self):
        return self.__account_number
    
    # setter for the account_number
    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    # getter for the balance
    @property
    def balance(self):
        return self.__balance
    
    # setter for the balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # M2) method for adding to the current balance
    def add_deposit(self, amount_to_add = 0):
        print("> Amount to Deposit    : ", end="")
        self.__balance = self.__balance + amount_to_add
        return amount_to_add
    
    # M3) method for deducting current balance
    def withdraw(self, amount_to_withdraw = 0):
        if amount_to_withdraw > self.__balance:
            print(f"> Amount to Withdraw   : {amount_to_withdraw}")
            print("> Withdrawal Process   : ",end="")
            return False
        else:
            self.__balance = self.__balance - amount_to_withdraw
            print(f"> Amount to Withdraw   : {amount_to_withdraw}")
            print("> Withdrawal Process   : ",end="")
            return True
    
    # M4) method for returning current balance only
    def display_balance(self):
        return (f"> Current Balance   : {self.__balance}")

    # M5) method for display account number and balance    
    def display_account_info(self):
        return (f"> Account Number    : {self.__account_number}"
                f"\n> Current Balance   : {self.__balance}")

# creating a BankAccount object
acc1 = BankAccount(121303, 1000)

print("\n--INITIAL ACCOUNT--")
print(acc1.display_account_info(), "\n") 
print(acc1.display_balance(), "\n")

print("--ACTIONS--")
print(acc1.add_deposit(1000)) 
print(acc1.display_balance(), "\n")

print(acc1.withdraw(500)) 
print(acc1.display_balance(), "\n") 

print("--FINAL ACCOUNT--")
print(acc1.display_account_info(), "\n") 
print(acc1.display_balance(), "\n")