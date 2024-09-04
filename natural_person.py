from client import Client

class NaturalPerson(Client):
    def __init__(self, name, birth_date, document, address):
        super().__init__(address)
        self.name = name
        self.document = document
        self.birth_date = birth_date
