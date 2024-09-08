import textwrap

from current_account import CurrentAccount, Withdraw
from deposit import Deposit
from natural_person import NaturalPerson

def menu():
    menu = """ \n
        ========= MENU ========
        [D]\tDeposit
        [W]\tWithdraw
        [S]\tStatement
        [NA]\tNew Account
        [SA]\tShow Accounts
        [NC]\tNew Client
        [SC]\tShow Clients
        [Q]\tQuit
        => """
    return input(textwrap.dedent(menu))

def make_transaction(clients, transaction_type: str):
    client, document = get_client(clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    value = float(input(f"Type the {'Deposit' if transaction_type == 'D' else 'Withdraw'} value: "))
    transaction = Deposit(value) if transaction_type == 'D' else Withdraw(value)

    account = recover_client_account(client)
    if not account:
        return

    client.make_transaction(account, transaction)

def recover_client_account(client):
    if not client.accounts:
        print("\n @@@ Client has no accounts! @@@")
        return

    account_number = input("Type the number from one of your accounts: ")
    account_chosen = [account for account in client.accounts if account.number == int(account_number)]
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
    print(f"\nBalance:\n\tR$ {account.account_balance:.2f}")
    print("==========================================")

def create_client(clients):
    client, document = get_client(clients)

    if client:
        print("There is already a user with this document")
        return

    name = input("Type your complete name: ")
    birth_date = input("Type your birth date (yyyy-mm-aa): ")
    address = input("Type your complete address (street - number - neighbourhood - city/state): ")

    client = NaturalPerson(
        name=name,
        birth_date=birth_date,
        address=address,
        document=document
    )

    clients.append(client)
    print("\n Client successful created!")

def filter_client(document, clients):
   filter_clients = [client for client in clients if client.document == document]
   return filter_clients[0] if filter_clients else None

def show_clients(users):
    print("============ USERS REGISTERED ON SYSTEM ===========\n")
    for user in users:
        print(f"User Name: {user.name} - Document: {user.document}\n")

def create_account(account_number, clients, accounts):
    client, document = get_client(clients)

    if not client:
        print("User Not Found!")
        return

    account = CurrentAccount.new_account(client=client, number=account_number)
    accounts.append(account)
    client.accounts.append(account)
    print("Account successful created!")

def show_accounts(accounts):
    if not accounts:
        print("There is no Accounts!")

    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))

def get_client(clients):
    document = input("Type your Document here: ")
    client = filter_client(document, clients)
    return client, document

def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "D":
            make_transaction(clients, option)

        elif option == "W":
            make_transaction(clients, option)

        elif option == "S":
            show_statement(clients)

        elif option == "NC":
            create_client(clients)

        elif option == "SC":
            show_clients(clients)

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