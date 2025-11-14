# Generate an ID
import random as generate

# Clears the screen
import os as screen

# Keeps the screen for a short time
import time

# Welcome the user
print("Hi! Welcome to your banking portal!")

# Get the user's account
name = input("What is your name? ")

# Account format
class Account:
    def __init__(self, holder, balance, ID, type):
        self.holder = holder
        self.balance = balance
        self.ID = ID if ID is not None else generate.randInt(0, 5000)
        self.type = type

    # Returns all the info about an account
    def features(self):
        return {
            "ID": self.id, 
            "Type": self.type, 
            "Price": self.price, 
            "Quantity": self.quantity
            }
    
    # Deposits to an account
    def deposit(self, deposit):
        deposit = input("How much do you want to deposit? ")
        if deposit > 0:
            self.balance += deposit
            print(f"Deposited ${deposit:.2f}.")
        else:
            print("Deposit must be positive.")

    # Withdraws from an account
    def withdraw(self, withdrawal):
        withdrawal = input("How much do you want to withdraw? ")
        if 0 < withdrawal <= self.balance:
            self.balance -= withdrawal
            print(f"Withdrew ${withdrawal:.2f}.")
        elif withdrawal > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal must be positive.")

    # Views all accounts
    def viewAccount(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.holder}")
        print(f"Account ID: {self.ID}")
        print(f"Balance: ${self.balance:.2f}")
        print("-----------------------")

# Starter accounts
accounts = [
    {'ID': 4327, 'Type': 'Checking', 'Balance': 100.00, 'Holder': "Asef Khan", 'ID': 2345},
    {'ID': 3915, 'Type': 'Savings', 'Savings': 30000.00, 'Count': "Afsana Afroze", 'ID': 2354},
]

# Creates a new account
def createAccount():
    print("---Creating a new account---")
                
    # Prompts for key info about account
    type = str(input("What kind of account do you want to have? "))
    amount = float(input("How mch money do you want to deposit in your new account? $"))
    holder = str(input("What name should the account be under? "))

    # Establishes the account
    account = Account(holder, amount, type)

    # Adds this account
    accounts.append(account.features)

    print(f"You have added a {account.type} account with ${account.balance} under the name of {account.holder}")

# Menu
def displayMenu():
    print("BANKING APP")
    print("What would you like to do?")
    print("1. View all balances")
    print("2. Deposit from any account")
    print("3. Withdraw from any account")
    print("4. Create a new bank account")
    print("5. Exit")
    userSelection()

# User selection
def userSelection():

    # The program stops running when the variable is False
    in_use = True
    
    choice = input("Which option do you want to pick? Please select a number 1-4. ")

    while in_use:
        
        # Which option runs?
        if choice == "1":
            print("You have decided to view the account's balance and history.")
            screen.system("clear")
            time.sleep(10)
            Account.viewAccount()
        elif choice == "2":
            print("You have decided to deposit to the account")
            screen.system("clear")
            time.sleep(10)
            Account.deposit()
        elif choice == "3":
            print("You have decided to withdraw from the account.")
            screen.system("clear")
            time.sleep(10)
            Account.withdraw()
        elif choice == "4":
            print("You have decided to create a new account.")
            screen.system("clear")
            createAccount()
        elif choice == "5":
            print("You have decided to delete an account.")
            screen.system("clear")
            time.sleep(10)
            Account.deleteAccount()
        elif choice == "6":
            print("Thank you for checking on your bank accounts.")
            
            # Exits out of the program
            break
        # To handle random inputs
        else:
            print("You have not selected a number 1-6.")

displayMenu()
