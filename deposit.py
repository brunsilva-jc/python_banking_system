from transaction import Transaction


class Deposit(Transaction):
    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        success_transaction = account.deposit(self.value)

        if success_transaction:
            account.statement.add_transaction(self)
