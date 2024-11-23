#module

pin = 2246
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
        