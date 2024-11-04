#python
def main():
    balance = 2500
    pin = 2246
    #total_deposits = 0
    #otal_withdrawals = 0

    print("WELCOME TO THE ATM!")

    # User Authentication
    for attempt in range(3):
        user_pin = int(input("Enter your PIN: "))
        if user_pin == pin:
            break
        else:
            print("Incorrect PIN. Try again.")
    else:
        print("Too many incorrect attempts. Access blocked.")
        return

    # Main Menu
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Change PIN")
        print("5.Check for withdrawable amount. Enter any amount:  ")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            # Check Balance
            print(f"Your current balance is: {balance}")

if __name__ == "__main__":
    main()

        