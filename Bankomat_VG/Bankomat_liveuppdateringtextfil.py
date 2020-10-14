import datetime


def accountAvailability(newAccount):
    with open('accounts.txt','r') as f:
        if str(newAccount) in f.read():
            return False

def createAccount():
    accountAvailable = False
    while accountAvailable == False:
        while True:
            try:
                newAccount = int(input('Enter your 6-digit account number> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        accountAvailable = accountAvailability(newAccount)
        if accountAvailable == False:
            print('Account number already in use.')
    with open('accounts.txt','a') as f:
        f.write(f'{newAccount} 0\n')
        print(f'Account {newAccount} created successfully.')
              
def gotoMainmenu():
    while True:
        while True:
            try:
                entry = int(input('****MAIN MENU****\n1. Create account\n2. Login\n3. End session\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry == 1:
            createAccount()
        if entry == 2:
            while True:
                try:
                    login = int(input('login(account number)> '))
                    break
                except ValueError:
                    print("Account number invalid.")
                else:
                    with open('accounts.txt','r') as f:
                        if login in f.read():
                            print('login successfull. Welcome!')
            gotoAccountmenu(login)
        if entry == 3:
            print('Session ended. Please come again.')
            break

def getbalancefromfile(accountNumber):
    with open('accounts.txt','r') as f:
        data = f.readlines()
        for line in data:
            if line.__contains__(str(accountNumber)):
                accountInfo=line
                balance=int(accountInfo.split(" ")[1])
                return balance
                    
def updateBalanceinFile(accountNumber, oldBalance, newBalance):
    with open('accounts.txt','r') as f:
        data = f.read()
        data = data.replace (f'{accountNumber} {oldBalance}', f'{accountNumber} {newBalance}')
        with open('accounts.txt','w') as f:
            f.write(data)
    
def loggTransaction(type, account, amount):
    if type == 'deposit':
        with open('transactions.txt','a') as f:
            timeNow = datetime.datetime.now()
            f.write(f'{timeNow.strftime("%c")} > account = {account} > deposit > {amount} kr\n')
    elif type == 'withdrawal':
            with open('transactions.txt','a') as f:
                timeNow = datetime.datetime.now()
                f.write(f'{timeNow.strftime("%c")} > account = {account} > withdrawal > {amount} kr\n')

def gotoAccountmenu(login):
    while True:
        while True:
            try:
                entry2 = int(input('****ACCOUNT MENU****\n1. Withdrawal\n2. Deposit\n3. Current balance\n4. Back to main menu\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry2 == 1:
            while True:
                try:
                    withdrawal = int(input('Amount to withdraw> '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            currentBalance = getbalancefromfile(login)
            if currentBalance < withdrawal:
                print('Your balance is too low.')
            else:
                newbalance = currentBalance - withdrawal
                updateBalanceinFile(login, currentBalance, newbalance)
                loggTransaction('withdrawal', login, withdrawal)
                print('Withdrawal complete.')
        if entry2 == 2:
            while True:
                try:
                    deposit = int(input('Amount to deposit> '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            currentBalance = getbalancefromfile(login)
            newbalance = currentBalance + deposit
            updateBalanceinFile(login, currentBalance, newbalance)
            loggTransaction('deposit', login, deposit)
            print('Deposit complete.')
        if entry2 == 3:
                print(f'Your balance is: {getbalancefromfile(login)} SEK')
        if entry2 == 4:
            break

gotoMainmenu()