class BankAccount:
    """A Simple Bank Account Class Demonstrating Encapsulation"""

    def __init__(self, account_holder, initial_balance = 0):
        #Public Attribute Can Be Accesed Anywhere Inside Or Outside The Class
        self.account_holder = account_holder
        #Private Attribute Cannot Accesed Directly Outside The Class
        self.__balance = initial_balance
        #Protected Attribute Is A Convention - It's Accessible But Shouldn't Be Modified Directly
        self._account_type = "Savings"

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} In Your Account. New Balance: ${self.balance}.")
        else:
            print(f"Deposition Failed! Amount Must Be In Positive Integers.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn ${amount} From Your Account. New Balance: ${self.balance}.")
            else:
                print(f"Withdrawal Failed! Please Enter The Amount Of Money You Have In Your Bank Account.")

    def get_balance(self):
        return self.balance
    
    def account_info(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.__balance}, Type: {self._account_type}."
    
my_acc = BankAccount("Azman", 1000)
print(my_acc.account_holder)
my_acc.account_holder = "Azman"
print(my_acc.account_holder)
print(my_acc.account_info())
print(my_acc.__balance)
