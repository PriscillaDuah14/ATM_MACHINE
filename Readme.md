# ATM MACHINE

## Authors
- Dorgbetor Catherena Emefa
(Github)[https://github.com/dorgbetorcatherena] | (LinkedIn) [https://www.linkedin.com/in/catherena-dorgbetor-13543b327]

- Priscilla Duah
(LinkedIn) [http://linkedin.com/in/priscilla-antwiwaa-duah-7485b532a]

## Project Overview
This project is a basic ATM simulation we created in Python. It lets users perform common banking tasks such as checking balance, depositing funds, withdrawing funds, and changing their PIN. We used Python fundamentals—like functions, loops, and conditional statements—to make the program interactive. It’s a great example of how to apply core programming skills to a practical scenario.

!(A picture of a simple ATM Machine) [https://play.google.com/store/apps/details?id=com.pms.atm.machine.virtualbank.simulator&gl=US]

## Key Features

1. User Authentication:

The program requires a 4-digit PIN to access the ATM.

Users have three attempts to enter the correct PIN before access is restricted.

2. Balance Check:

Users can quickly check their balance, which is displayed in a clear format.

3. Deposit Funds:

Users can deposit an amount, provided it’s positive, which is added to their balance.

The program confirms the new balance after each successful deposit.

4. Withdraw Funds:

Users can withdraw an amount if they have sufficient funds.

Positive amounts are required, and the program checks that the balance covers the transaction.

5. Change PIN:

Users can update their PIN by first confirming their current PIN.

The new PIN must be a 4-digit integer, and users confirm it to ensure no mistakes.

6. Check for withdrawable amount:
The user is able to check if an amount entered is withdrawable or not.

7. Exit:

Users can exit the program at any time, receiving a summary of their total deposits and withdrawals.

## Requirements

Python 3.x installed

Basic understanding of Python programming

## How to Use 

1. Run the Program:

Save the script [control_flow_atm.py file] and run it using the command: python control_flow_atm.py.

2. Authenticate:

When prompted, enter your 4-digit PIN.

If you enter it incorrectly three times, the program will restrict access.

3. Main Menu Options:

After authentication, the main menu displays the following options:

1 for checking balance.

2 for depositing funds.

3 for withdrawing funds.

4 for changing your PIN.

5 to check for withdrawable amount

6 to exit the program.


4. Select an Option:

Enter the number that corresponds to the action you want to perform.

Follow the prompts for each option.

6. Exit:

Choose option 6 to exit.

Upon exit, the program will display a final summary of your total deposits and withdrawals.

## Code Walkthrough

1. User Authentication:

Users get three chances to enter the correct PIN; if they fail, access is blocked.

2. Main Menu:

The program continuously displays the main menu until users choose to exit.

3. Option Details:

Check Balance: Shows the current balance.

Deposit Funds: Prompts for a deposit amount; updates the balance if valid.

Withdraw Funds: Prompts for a withdrawal amount; ensures the balance covers it.

Change PIN: Confirms the current PIN, then prompts for and verifies a new 4-digit PIN.

Check amount withdrawable: Confirms if the user can withdraw an amount of money or not.

Exit: Summarizes total deposits and withdrawals before closing the program.

4. Error Handling:

The program includes error messages for invalid PIN entries, invalid choices, and incorrect deposit or withdrawal amounts, guiding users to correct the errors.

## Sample Program Run
WELCOME TO THE ATM!

Enter your PIN: **
Incorrect PIN. Try again.
Enter your PIN: **
Incorrect PIN. Try again.
Enter your PIN: **


Main Menu:
1. Check Balance
2. Deposit Funds
3. Withdraw Funds
4. Change PIN
5. Check for withdrawable amount
6. Exit
Choose an option (1-6): 1
Your current balance is: 2500

Choose an option (1-6): 2
Enter amount to deposit: 1000
New balance after deposit: 35000

Choose an option (1-6): 3
Enter amount to withdraw: 500
New balance after withdrawal: 2500

Choose an option (1-6): 4
Enter your current PIN: **
Enter your new 4-digit PIN: **
Confirm your new PIN: **
Your PIN has been changed successfully.

Choose an option (1-6): 5
Checking to see how much is withdrawable. Enter any amount: 49
You cannot withdraw less $50. Please try again.


Choose an option (1-6): 6
Thank you for using the ATM. You made a total deposit of 1000 and a total withdrawal of 500.

## Possible Improvements

In the future, we'd like to:

Add Persistent Data Storage: Use a database or file to save account details for a more realistic experience.

Track Transaction History: Display past deposits, withdrawals, and balance checks.

Enhance Security: Introduce stronger PIN requirements or add features like biometric authentication.