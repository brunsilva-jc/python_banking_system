from abc import abstractproperty, abstractclassmethod


class Transaction:

    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass