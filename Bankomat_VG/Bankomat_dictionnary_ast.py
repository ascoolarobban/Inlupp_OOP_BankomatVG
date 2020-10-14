import ast
import datetime

with open('accounts.txt','r') as f:
    contents = f.read()
    accountInfo = ast.literal_eval(contents)
    
avsluta = False
while avsluta == False:
    while True:
        try:
            entry1 = int(input('****MAIN MENU****\n1. Create account\n2. Login\n3. End session\n> '))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    if entry1 == 1:
        newAccount = int(input('Enter your 6-digit account number> '))
        while newAccount in accountInfo.keys():
            newAccount = int(input('Account already exists, Try again. Enter your 6-digit account number> '))
        accountInfo[newAccount] = 0 
        print(f'Account {newAccount} created successfully.')
    if entry1 == 2:
        login = int(input('login(account number)> '))
        while login not in accountInfo.keys():
            login = int(input('Account number does not exist. Try again.\nlogin(account number)> '))
        print('Login successfull.')
        backtomain = False
        while backtomain == False:
            entry2 = int(input('****ACCOUNT MENU****\n1. Withdrawal\n2. Deposit\n3. Current balance\n4. Back to main menu\n> '))
            currentBalance = accountInfo[login]
            if entry2 == 1:
                withdrawal = int(input('Amount to withdraw> '))
                if currentBalance < withdrawal:
                    print('Your balance is too low.')
                else:
                    newbalance = currentBalance - withdrawal
                    accountInfo[login] = newbalance
                    with open('transactions.txt','a') as f:
                        timeNow = datetime.datetime.now()
                        f.write(f'{timeNow.strftime("%c")} > account = {login} > withdrawal > {withdrawal} kr\n')
                    print('Withdrawal complete.')
            if entry2 == 2:
                deposit = int(input('Amount to deposit> '))
                newbalance = currentBalance + deposit
                accountInfo[login] = newbalance
                with open('transactions.txt','a') as f:
                        timeNow = datetime.datetime.now()
                        f.write(f'{timeNow.strftime("%c")} > account = {login} > deposit > {deposit} kr\n')
                print('Deposit complete.')
            if entry2 == 3:
                print(f'Your balance is: {currentBalance} SEK')
            if entry2 == 4:
                backtomain = True
    if entry1 == 3:
        print('Good bye.')
        avsluta = True

with open('accounts.txt','w') as f:
    f.write(str(accountInfo))


