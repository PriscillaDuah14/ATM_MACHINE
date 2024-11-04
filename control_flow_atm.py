#!/usr/bin/python
def main():
    balance = 2500
    pin = 2246
    total_deposits = 0
    total_withdrawals = 0

    print("WELCOME TO THE ATM!")

    # User Authentication
    for attempt in range(3):
        user_pin = int(input("Enter your PIN: "))
        if user_pin == pin:
            break
        else:
            print("Incorrect PIN. Try again.")
    else:
        print("Too many incorrect attempts. Access blocked!.")
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
            print(f"Your current balance is: ${balance}")


        elif choice == '2':
            # Deposit Funds
            deposit_amount = float(input("Enter the amount to deposit: "))
            balance += deposit_amount
            total_deposits += deposit_amount
            
            print(f"Deposit successful. Your new balance is: ${balance}")
            

        elif choice == '3':
            # Withdraw Funds
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                total_withdrawals += withdraw_amount
                print(f"Withdrawal successful. Your new balance is: ${balance}")
                
            else:
                print("Insufficient funds.")

                return
                
        elif choice == '4':
            # Change PIN
            current_pin = int(input("Enter your current PIN: "))
            if current_pin == pin:
                new_pin = int(input("Enter your new 4-digit PIN: "))
                if 1000 <= new_pin <= 9999:
                    confirm_pin = int(input("Confirm your new PIN: "))
                    if new_pin == confirm_pin:
                        pin = new_pin
                        print("Your PIN has been changed successfully.")
                    else:
                        print("PINs do not match. Try again.")
                else:
                    print("New PIN must be a 4-digit integer.")
            else:
              print("Current PIN is incorrect.")
        
        
        elif choice == '5':
            withdraw_amount = int(input("Checking to see how much is withdrawable.Enter any amount: "))
            if withdraw_amount < 50:
            
                print("You can't withdraw less than $50 . Please try again.")     
        
        
        elif choice == '6':            
            # Exit
            print(f"Thank you for using the ATM. You made a total deposit of {total_deposits} and a total withdrawal of {total_withdrawals}.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()             
