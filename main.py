from datetime import datetime, date, timedelta, timezone, time

menu = """
    [D] Deposit
    [W] Withdraw
    [S] Statement
    [Q] Quit
=> """

balance = 0
limit = 1000
statement = ""
withdraw_number = 0
WITHDRAW_LIMIT = 3

date_now = datetime.now()

while True:
    option = input(menu)

    if option == "D":
        value = float(input("Enter the deposit amount: "))

        if value > 0:
            balance += value
            statement += f"Deposit: $ {value:.2f} {date_now}\n"
            print("======================================")
            print(f"Successful Deposit: $ {value} {date_now} ".center(10))
            print("======================================")

        else:
            print("Operation failed! The value is invalid")

    elif option == "W":
        value = float(input("Enter the withdrawal amount:"))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdraw = withdraw_number >= WITHDRAW_LIMIT

        if exceeded_balance:
            print("Operation failed! You don't have enough balance!")

        elif exceeded_limit:
            print("Operation failed! Withdrawal amount exceeds limit")

        elif exceeded_withdraw:
            print(f"Operation failed! Maximum number of withdrawals exceeded for today: {date_now}")

        elif value > 0:
            balance -= value
            statement += f"Withdrawal: $ {value:.2f} {date_now}\n"
            withdraw_number += 1
            print("======================================")
            print(f"Successful withdrawal: $ {value} {date_now}".center(10))
            print("======================================")

        else:
            print("Operation failed! The value is invalid")

    elif option == "S":
        print("\n============== STATEMENT ==============")
        print("No transactions were made" if not statement else statement)
        print(f"\nBalance: $ {balance:.2f}")
        print(f"Date: {date_now}")
        print("=======================================")


    elif option == 'Q':
        break;

    else:
        print("Invalid operation! select a valid option")






