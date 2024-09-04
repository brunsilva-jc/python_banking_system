from msilib.schema import Property
from datetime import datetime
from statement import Statement

from main import date_now


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._agency = "0001"
        self._number = number
        self._client = client
        self._statement = Statement()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    @Property
    def balance(self):
        return self._balance

    @Property
    def number(self):
        return self._number

    @Property
    def agency(self):
        return  self._agency

    @Property
    def client(self):
        return self._client

    @Property
    def statement(self):
        return self._statement


    def withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operation failed! You don't have enough balance! @@@")

        elif value > 0:
            self.balance -= value
            print(f"\nSuccessful withdrawal: $ {value} {datetime.now}".center(10))
            return True

        else:
            print("\n @@@ Operation failed! The value is invalid. @@@")

        return False

    def deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"\nSuccessful Deposit: $ {value} {date_now} ".center(10))
        else:
            print("\n @@@ Operation failed! The value is invalid @@@")
            return False
        return True

