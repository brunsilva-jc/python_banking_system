from transaction import Transaction


class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        self._value

    def register(self, account):
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.statement.add_transaction(self)