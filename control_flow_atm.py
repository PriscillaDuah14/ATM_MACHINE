#!/usr/bin/python
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
            # Exit
            print(f"Thank you for using the ATM. You made a total deposit of {total_deposits} and a total withdrawal of {total_withdrawals}.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()             