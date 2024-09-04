from datetime import datetime

class Statement:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )