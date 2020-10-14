#Jonathans OOP Bankomat! 

#Här är min slutgiltiga version för inlämningsuppgift 1. 

import datetime

#CLASSES

class Textfile:

    def __init__(self,name):
        self._name = name

    def Name(self):
        return self._name

    def Write(self, string):
        with open(f'{self.Name()}','w') as f:
            f.write(string)

    def Append(self, string):
        with open(f'{self.Name()}','a') as f:
            f.write(string)

    def ContentIntoString(self):
        with open(f'{self.Name()}','r') as f:
            string = f.read()
            return string

    def ContentIntoList(self):  #Each line in the text file fills one element in the list.
        with open(f'{self.Name()}','r') as f:
            list = f.readlines()
            return list

    def GetLineContainingString(self, string): #Look for a string in each line of the text file return the first line containing it.
        for line in self.ContentIntoList():
            if string in line:
                return line

    def IsStringInFile(self, String):
        if String in self.ContentIntoString():
            return True
        else:
            return False

class Account:

    def __init__(self,accountNumber, balance):
        self._accountNumber = accountNumber
        self._balance = balance
    
    def AccountNumber(self):
        return self._accountNumber

    def Balance(self):
        return self._balance

    def ChangeBalance(self, NewBalance):
        self._balance = NewBalance
        
    def InitializeBalance(self): #Takes balance from textfile into program after login.
        self.ChangeBalance(self.BalanceFromFile())

    def AppendAccountToFile(self):
        AccountString=f'{self._accountNumber} {self._balance}\n'
        AccountTxtFile.Append(AccountString)
            
    def IsAccountAvailable(self):
            if self.AccountNumber() in AccountTxtFile.ContentIntoString():
                return False
            else:
                return True
    
    def AccountLine(self):  #Returns the account numbers line in text file.
        return AccountTxtFile.GetLineContainingString(self.AccountNumber())
           
    def BalanceFromFile(self): 
        balance=int(self.AccountLine().split(" ")[1])   #Splits a string into a list of elements using spacebar as a splitpoint. We take the 2nd element (index 1) to get the balance.
        return balance

    def UpdateBalanceInFile(self):
        CurrentAccountString = f'{self.AccountNumber()} {self.BalanceFromFile()}'
        NewAccountString = f'{self.AccountNumber()} {self.Balance()}'
        AccountFile = AccountTxtFile.ContentIntoString().replace(CurrentAccountString, NewAccountString)
        AccountTxtFile.Write(AccountFile)
    
    def loggTransaction(self, type, amount):
        timeNow = datetime.datetime.now()
        if type == 'deposit':
            DepositTransactionString = f'{timeNow.strftime("%c")} > account = {self.AccountNumber()} > deposit > {amount} kr\n'
            TransactionTxtFile.Append(DepositTransactionString)
        elif type == 'withdrawal':
            WithdrawalTransactionString = f'{timeNow.strftime("%c")} > account = {self.AccountNumber()} > withdrawal > {amount} kr\n'
            TransactionTxtFile.Append(WithdrawalTransactionString)

    def withdraw(self, amount):
        if self.Balance() < amount:
            print('Your balance is too low.')
        else:
            NewBalance = self.Balance() - int(amount)
            self.ChangeBalance(NewBalance)
            self.UpdateBalanceInFile()
            self.loggTransaction('withdrawal', amount)
            
    def deposit(self, amount):
        NewBalance = self.Balance() + int(amount)
        self.ChangeBalance(NewBalance)
        self.UpdateBalanceInFile()
        self.loggTransaction('deposit', amount)

class LoggingIn:

    def __init__(self,login):
        self._login = login

    def login(self):
        return self._login

    def CheckIfLoginIsKey(self):
        return AccountTxtFile.IsStringInFile(str(self.login()))

    def InitializeAccount(self):
        currentAccount = Account(self.login(), 0)
        currentAccount.InitializeBalance()
        return currentAccount

#Text Files

AccountTxtFile=Textfile('accounts.txt')
TransactionTxtFile=Textfile('transactions.txt')

#INPUT-Functions

def registerAccount():
    accountAvailable = False
    sixdigits = False
    while accountAvailable == False or sixdigits == False:
        desiredAccount = 100000
        while True:
                try:
                    desiredAccount = input('Enter your 6-digit account number> ')
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        newAccount = Account(desiredAccount, 0)
        accountAvailable = newAccount.IsAccountAvailable()
        if int(desiredAccount) > 99999 or int(desiredAccount) < 999999:
            sixdigits = True
        if accountAvailable == False:
             print('Account number already in use. Try again.')
             del newAccount
    newAccount.AppendAccountToFile()
    print(f'Account {desiredAccount} created successfully.')

def Mainmenu():
    while True:
        while True:
            try:
                entry = int(input('****MAIN MENU****\n1. Create account\n2. Login\n3. End session\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry == 1:
            registerAccount()
        if entry == 2:
            entranceUnlocked = False
            while entranceUnlocked == False:
                while True:
                    try:
                        login = input('login(account number)> ')
                        Initializer = LoggingIn(login)
                        break
                    except ValueError:
                        print("Account number invalid.")
                entranceUnlocked = Initializer.CheckIfLoginIsKey()
            print('login successfull. Welcome!')
            gotoAccountmenu(Initializer.InitializeAccount())

        if entry == 3:
            print('Session ended. Please come again.')
            break



def gotoAccountmenu(Account):
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
                    Account.withdraw(int(input('Amount to withdraw> ')))
                    print('Withdrawal complete.')
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        if entry2 == 2:
            while True:
                try:
                    Account.deposit(input('Amount to deposit> '))
                    print('Deposit complete.')
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        if entry2 == 3:
                print(f'Your balance is: {Account.Balance()} SEK')
        if entry2 == 4:
            break

#Run program:

Mainmenu()

