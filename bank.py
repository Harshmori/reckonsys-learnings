import csv

class Account():
    def __init__(self, acc_no, name, contact, balance):
        self.acc_no = acc_no
        self.name = name
        self.contact = contact
        self.transactions = [] 
        self.transactions.append(("Initial deposit", balance))
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Amount must be positive"
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        return True, self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            return False, "Amount must be positive"
        if amount > self.balance:
            return False, "Insufficient balance"
        self.balance -= amount
        self.transactions.append(("Withdrawal", -amount))
        return True, self.balance

    def get_statement(self):
        print(f"\nAccount Statement for {self.name} (Acc: {self.acc_no})")
        print("--------------------------------------------")
        print("Transaction Type    Amount      Balance")
        print("--------------------------------------------")
        
        running_balance = 0
        for trans_type, amount in self.transactions:
            running_balance += amount
            print(f"{trans_type}-------{amount}-------{running_balance}")
    

class Bank():
    def __init__(self):
        self.accounts = []
        self.load_accounts()

    def load_accounts(self):
        try:
            with open('accounts.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    acc = Account(row['acc_no'], row['name'], row['contact'], float(row['balance']))
                    acc.transactions = eval(row['transactions']) 
                    self.accounts.append(acc)
        except FileNotFoundError:
            with open('accounts.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['acc_no', 'name', 'contact', 'balance', 'transactions'])
                writer.writeheader()

    def save_accounts(self):
        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['acc_no', 'name', 'contact', 'balance', 'transactions'])
            writer.writeheader()
            for acc in self.accounts:
                writer.writerow({
                    'acc_no': acc.acc_no,
                    'name': acc.name,
                    'contact': acc.contact,
                    'balance': acc.balance,
                    'transactions': str(acc.transactions)
                })

    def create_account(self, acc_no, name, contact, balance):
        acc = Account(acc_no, name, contact, balance)
        self.accounts.append(acc)
        return acc

    def create_account(self, acc_no, name, contact, balance):
        if any(acc.acc_no == acc_no for acc in self.accounts):
            return None, "Account number already exists"
        if balance < 0:
            return None, "Initial balance cannot be negative"
        if not contact.isdigit():
            return None, "Contact should contain only numbers"
            
        acc = Account(acc_no, name, contact, balance)
        self.accounts.append(acc)
        return acc, "Account created successfully"
    
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
            acc, message = bank.create_account(acc_no, name, contact, balance)
            if acc:
                print(message)
                bank.save_accounts()
            else:
                print(f"Error: {message}") 
                print("Please enter a valid number for balance")

        elif task == 2:
            acc_no = input("Enter account number: ")
            amount = int(input("Enter amount to deposit: "))
            acc = bank.get_account(acc_no)
            if acc:
                success, result = acc.deposit(amount)
                if success:
                    print(f"Deposit successful. New balance is {result}")
                else:
                    print(f"Deposit failed: {result}")
                bank.save_accounts()
            else:
                print("Account not found")

        elif task == 3:
            acc_no = input("Enter account number: ")
            amount = int(input("Enter amount to withdraw: "))
            acc = bank.get_account(acc_no)
            if acc:
                success, result = acc.withdraw(amount)
                if success:
                    print(f"Withdrawal successful. New balance is {result}")
                else:
                    print(f"Withdrawal failed: {result}")
                bank.save_accounts()
            else:
                print("Account not found")

        elif task == 4:
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                acc.get_statement()
            else:
                print("Account not found")
            bank.save_accounts()
        elif task == 5:
            flag = 0


if __name__=="__main__":
    main()
