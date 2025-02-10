class Account():
    def __init__(self, acc_no, name, contact, balance):
        self.acc_no = acc_no
        self.name = name
        self.contact = contact
        self.transactions = [] 
        self.transactions.append(("Initial deposit", balance))
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("Withdrawal", -amount))
            return self.balance
        else:
            return f"account does not have enough balance to make this withdrawal"

    def get_statement(self):
        print(f"\nAccount Statement for {self.name} (Acc: {self.acc_no})")
        print("--------------------------------------------")
        print("Transaction Type    Amount      Balance")
        print("--------------------------------------------")
        
        running_balance = 0
        for trans_type, amount in self.transactions:
            running_balance += amount
            print(f"{trans_type}      {amount}       {running_balance}")
    

class Bank():
    def __init__(self):
        self.accounts = []
    
    def create_account(self, acc_no, name, contact, balance):
        acc = Account(acc_no, name, contact, balance)
        self.accounts.append(acc)
        return acc
    
    def get_account(self, acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None


def main():
    bank = Bank()
    flag = 1
    while(flag):
        print("hello, press any one of the following digits to perform corresponding task")
        print("1 - create account")
        print("2 - deposit money")
        print("3 - withdraw money")
        print("4 - view account statement")
        print("5 - exit")


        task = int(input())

        if task == 1:
            name = input("Enter name: ")
            contact = input("Enter contact: ")
            acc_no = input("Enter account number: ")
            balance = int(input("Enter initial balance: "))
            acc = bank.create_account(acc_no, name, contact, balance)
            print(f"account created successfully ")
        elif task == 2:
            acc_no = input("Enter account number: ")
            amount = int(input("Enter amount to deposit: "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.deposit(amount)
                print(f"New balance is {acc.balance}.")
            else:
                print("Account not found")
                acc.deposit(amount)
        elif task == 3:
            acc_no = input("Enter account number: ")
            amount = int(input("Enter amount to withdraw: "))
            acc = bank.get_account(acc_no)
            if acc:
                print(f"New balance is {acc.balance}.")
            else:
                print("Account not found")
            acc.withdraw(amount)
        elif task == 4:
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                acc.get_statement()
            else:
                print("Account not found")
        elif task == 5:
            flag = 0


if __name__=="__main__":
    main()
