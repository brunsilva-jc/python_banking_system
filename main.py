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
WITHDRAW_LIMIT = 5

while True:
    option = input(menu)

    if option == "D":
        value = float(input("Enter the deposit amount: "))

        if value > 0:
            balance += value
            statement += f"Deposit: $ {value:.2f}\n"
            print("======================================")
            print(f"Successful Deposit: $ {value}".center(10))
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
            print("Operation failed! Maximum number of withdrawals exceeded")

        elif value > 0:
            balance -= value
            statement += f"Withdrawal: $ {value:.2f}\n"
            withdraw_number += 1
            print("======================================")
            print(f"Successful withdrawal: $ {value}".center(10))
            print("======================================")

        else:
            print("Operation failed! The value is invalid")

    elif option == "S":
        print("\n============== STATEMENT ==============")
        print("No transactions were made" if not statement else statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("=======================================")


    elif option == 'Q':
        break;

    else:
        print("Invalid operation! select a valid option")






