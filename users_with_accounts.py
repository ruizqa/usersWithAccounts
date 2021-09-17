class BankAccount:
    Accounts = []
    def __init__(self,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.Accounts.append(self)
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    def yield_interest(self):
        if self.balance >0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def printAccounts(cls):
        print(f"\nThere are {len(cls.Accounts)} bank accounts:")
        for i in cls.Accounts:
            print(f"\nAccount #{cls.Accounts.index(i)+1}")
            i.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    #adding an account:
    def addAccount(self,int_rate,balance=0):
        self.accounts.append(BankAccount(int_rate,balance))
        return self
    #deleting an account
    def deleteAccount(self,index=-1):
        self.accounts.pop(index)
        return self
    # adding the deposit method
    def make_deposit(self, acc_index,amount):	# takes an argument that is the amount of the deposit
        self.accounts[acc_index].balance += amount
        return self
    def make_withdrawal(self,acc_index,amount):
        if amount <= self.accounts[acc_index].balance:
            self.accounts[acc_index].balance -= amount
            
        else:
            print (f"The amount requested is higher than the account balance (${self.accounts[acc_index].balance})")
        return self
    def display_user_balance(self,acc_index):
        print(f"User: {self.name}, Account: {acc_index+1}, Balance: ${self.accounts[acc_index].balance}")
        return self
    def transfer_money(self, other_user, amount,acc_index1,acc_index2):
        self.accounts[acc_index1].balance -= amount
        other_user.accounts[acc_index2].balance += amount
        return self


user1 = User("Jim", "jim@hi.com")
user2 = User("Jerome", "jerome@hi.com")
user1.addAccount(0.1,1500).addAccount(0.2,25).make_deposit(0,10).make_withdrawal(1,5)
user2.addAccount(0.1,50).addAccount(0.1,5).make_deposit(0,100).make_withdrawal(1,4)
user1.transfer_money(user2,70,0,0)
user1.display_user_balance(0)
user2.display_user_balance(0)
user1.display_user_balance(1)
user2.display_user_balance(1)

