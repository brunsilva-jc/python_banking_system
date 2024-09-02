import textwrap
from datetime import datetime
from typing import Final

from account import Account
from user import User

date_now = datetime.now()

def menu():
    menu = """ \n
        ========= MENU ========
        [D]\tDeposit
        [W]\tWithdraw
        [S]\tStatement
        [NA]\tNew Account
        [SA]\tShow Accounts
        [NU]\tNew User
        [SU]\tShow Users
        [Q]\tQuit
        => """
    return input(textwrap.dedent(menu))

def deposit(balance, value, statement):
    if value > 0:
        balance += value
        statement += f"Deposit: $ {value:.2f} {date_now}\n"
        print("======================================")
        print(f"Successful Deposit: $ {value} {date_now} ".center(10))
        print("======================================")
        return balance , statement

    else:
        print("Operation failed! The value is invalid")

def withdraw(*, balance, value, statement, limit, withdraw_number, withdraw_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    print(withdraw_number , withdraw_limit)
    exceeded_withdraw = withdraw_number >= withdraw_limit

    if exceeded_balance:
        print("Operation failed! You don't have enough balance!")
        return balance, statement, withdraw_number

    elif exceeded_limit:
        print("Operation failed! Withdrawal amount exceeds limit")
        return balance, statement, withdraw_number

    elif exceeded_withdraw:
        print(f"Operation failed! Maximum number of withdrawals exceeded for today: {date_now}")
        return balance, statement, withdraw_number

    elif value > 0:
        balance -= value
        statement += f"Withdrawal: $ {value:.2f} {date_now}\n"
        withdraw_number += 1
        print("======================================")
        print(f"Successful withdrawal: $ {value} {date_now}".center(10))
        print("======================================")
        return balance, statement , withdraw_number

    else:
        print("Operation failed! The value is invalid")

def show_statement(balance, /, *, statement):
    print("\n============== STATEMENT ==============")
    print("No transactions were made" if not statement else statement)
    print(f"\nBalance: $ {balance:.2f}")
    print(f"Date: {date_now}")
    print("=======================================")

def create_user(users):
    document = input("Type your document (only numbers): ")
    user = filter_user(document, users)

    if user is  None:
        user_name = input("Type your complete name: ")
        user_birth = input("Type the day of birth (yyyy-mm-dd): ")
        user_address = input("Type your Address: (Street, Neighbourhood, City-State):  ")
        user = User(user_name, document,user_birth, user_address)

        users.append(user)
        print("User successful created!")

    else:
        print("There is already a user with this document")

def filter_user(document, users):
    for user in users:
        if user.document == document:
            return user
        else:
            return None

def show_users(users):
    print("============ USERS REGISTERED ON SYSTEM ===========\n")
    for user in users:
        print(f"User Name: {user.name} - Document: {user.document}\n")

def create_account(agency, account_number, users):
    document = input("Type your Document here: ")
    user = filter_user(document, users)

    if user:
        account = Account(agency, account_number, user)
        print("\n Account successful created! ")
        return account

    print("User Not Found!")

def show_accounts(accounts):
    print(accounts)
    print("======== Accounts registered on the system =======")
    for account in accounts:
        print(f"Agency - {account.agency}, Number: {account.number}, User: {account.user.name}")

def main():
    WITHDRAW_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 1000
    statement = ""
    withdraw_number = 0

    users = []
    accounts = []

    while True:
        option = menu()

        if option == "D":
            value = float(input("Enter the deposit amount: "))
            balance, statement = deposit(balance, value, statement)

        elif option == "W":
            value = float(input("Enter the withdrawal amount:"))
            balance, statement , withdraw_number = withdraw(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                withdraw_number=withdraw_number,
                withdraw_limit=WITHDRAW_LIMIT
            )

        elif option == "S":
            show_statement(balance, statement=statement)

        elif option == "NU":
            create_user(users)

        elif option == "SU":
            show_users(users)

        elif option == "NA":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)
            accounts.append(account)

        elif option == "SA":
            show_accounts(accounts)

        elif option == "Q":
            break

        else:
            print("Invalid operation! select a valid option")

main()