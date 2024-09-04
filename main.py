import textwrap
from datetime import datetime

from account import *
from client import Client
from deposit import Deposit
from transaction import Transaction
from withdraw import Withdraw

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

def deposit(clients):
    document = input("Type your Document here: ")
    client = filter_client(document, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    value = float(input("Type the deposit value: "))
    transaction = Deposit(value)

    account = recover_client_account(client)
    if not account:
        return

    client.make_transaction(account, transaction)

def withdraw(clients):
    document = input("Type your Document here: ")
    client = filter_client(document, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    value = float(input("Type the withdraw value: "))
    transaction = Withdraw(value)

    account = recover_client_account(client)
    if not account:
        return

    client.make_transaction(account, transaction)

def recover_client_account(client):
    if not client.accounts:
        print("\n @@@ Client has no accounts! @@@")
        return

    account_number = input("Type the number from one of your accounts: ")
    account_chosen = [account for account in client.accounts if account.number == account_number]
    return account_chosen[0]

def show_statement(clients):
    document = input("Type your Document here: ")
    client = filter_client(document, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    account = recover_client_account(client)
    if not account:
        return

    print("\n============== STATEMENT ==============")
    transactions = account.statement.transactions

    extract = ""
    if not transactions:
        extract = "No transaction made!"
    else:
        for transaction in transactions:
            extract += f"\n{transaction['type']}: \n\tR${transaction['value']:.2f}"

    print(extract)
    print(f"\nBalance:\n\tR$ {account.balance:.2f}")
    print("==========================================")

def create_user(users):
    document = input("Type your document (only numbers): ")
    user = filter_client(document, users)

    if user is  None:
        user_name = input("Type your complete name: ")
        user_birth = input("Type the day of birth (yyyy-mm-dd): ")
        user_address = input("Type your Address: (Street, Neighbourhood, City-State):  ")
        user = Client(user_address)

        users.append(user)
        print("User successful created!")

    else:
        print("There is already a user with this document")

def filter_client(document, clients):
   filter_clients = [client for client in clients if client.document == document]
   return filter_clients[0] if filter_clients else None

def show_users(users):
    print("============ USERS REGISTERED ON SYSTEM ===========\n")
    for user in users:
        print(f"User Name: {user.name} - Document: {user.document}\n")

def create_account(account_number, clients, accounts):
    document = input("Type your Document here: ")
    client = filter_client(document, clients)

    if client:
        account = Account(account_number, client)
        print("\n Account successful created! ")
        return account

    print("User Not Found!")

def show_accounts(accounts):
    print(accounts)
    print("======== Accounts registered on the system =======")
    for account in accounts:
        print(f"Agency - {account.agency}, Number: {account.number}, User: {account.user.name}")

def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "D":
            deposit(clients)

        elif option == "W":
            withdraw(clients)

        elif option == "S":
            show_statement(clients)

        elif option == "NU":
            create_user(clients)

        elif option == "SU":
            show_users(clients)

        elif option == "NA":
            account_number = len(accounts) + 1
            create_account(account_number, clients, accounts)

        elif option == "SA":
            show_accounts(accounts)

        elif option == "Q":
            break

        else:
            print("Invalid operation! select a valid option")

main()