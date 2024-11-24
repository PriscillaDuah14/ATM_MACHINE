#creating a class for the acccount
class Account:
    def __init__(self, account_number, account_holder, password, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount!")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def verify_password(self, password):
        return self.password == password


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, password):
        if account_number in self.accounts:
            print("Account number already exists!")
        else:
            self.accounts[account_number] = Account(account_number, account_holder, password)
            print(f"Account for {account_holder} created successfully!")

    def access_account(self, account_number, password):
        account = self.accounts.get(account_number)
        if account:
            if account.verify_password(password):
                print(f"Accessing account for {account.account_holder}.")
                return account
            else:
                print("Incorrect password!")
                return None
        else:
            print("Account not found!")
            return None

    def start(self):
        while True:
            print("\n--- Welcome to the ATM ---")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                account_number = input("Enter new account number: ")
                account_holder = input("Enter account holder name: ")
                password = input("Set a password for the account: ")
                self.create_account(account_number, account_holder, password)
            elif choice == "2":
                account_number = input("Enter your account number: ")
                password = input("Enter your password: ")
                account = self.access_account(account_number, password)
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

    def account_menu(self, account):
        while True:
            print(f"\n--- Account Menu for {account.account_holder} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please try again.")


# Running the ATM
atm = ATM()
atm.start()