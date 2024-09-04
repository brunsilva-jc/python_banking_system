from datetime import datetime

from account import Account
from withdraw import Withdraw


class CurrentAccount(Account):
    def __init__(self, number, client, limit=500, withdraw_limit=5):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit= withdraw_limit

    def withdraw(self, value):
        withdraw_number = len(
            [transaction for transaction in self.statement.transactions if transaction["type"] == Withdraw.__name__]
        )

        exceeded_limit = value > self.limit
        exceeded_withdraw = withdraw_number >= self.withdraw_limit

        if exceeded_limit:
            print("\n @@@ Operation failed! Withdrawal amount exceeds limit. @@@")

        elif exceeded_withdraw:
            print(f"Operation failed! Maximum number of withdrawals exceeded for today: {datetime.now()}")

        else:
            return super().withdraw(value)

        return False

    def __str__(self):
        return  f"""\
        Agency:\t{self.agency}
        C/A:\t{self.number}
        Account Holder:\t{self.client.name}
        """