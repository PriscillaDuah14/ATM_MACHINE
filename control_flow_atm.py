

def main():
    balance = 2500
    pin = 2246
    total_deposits = 0
    total_withdrawals = 0

    print("WELCOME TO THE ATM!")

    # User Authentication
    for attempt in range(3):
        print(f"Attempts left: {3 - attempt}")
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
        print("5. Transaction History")
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
            if withdraw_amount < 50:
                 print("You cannot withdraw less than $50.Please try again!")
                 continue
            
            elif withdraw_amount > balance:
                print("Insufficient funds.")
            elif withdraw_amount != 50:
                balance -= withdraw_amount
                total_withdrawals += withdraw_amount

            print(f"Withdrawal successful. Your new balance is: ${balance}")

                                   
                
            continue
                
        elif choice == '4':
            # Change PIN
            import pin
            pin.current_pin
               
            
        #Transaction history
        
        elif choice == '5':
            print("\nTransaction History:")
            print(f"Deposits: ${total_deposits}")
            print(f"Withdrawals: ${total_withdrawals}")
            print(f"Current Balance: ${balance}")
            print(f"Total Balance: ${balance}")
            print(f"Total Transactions: {total_deposits + total_withdrawals}")

            
    
            continue
        
        elif choice == '6':           
            # Exit
            print(f"Thank you for using the ATM. You made a total deposit of ${total_deposits} and a total withdrawal of ${total_withdrawals}.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()             