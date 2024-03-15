class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        type(self).all.append(self)

    def contracts(self):
        return self._contracts
    
    def add_contract(self, contract):   
        self._contracts.append(contract)

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        type(self).all.append(self)

    def contracts(self):
        return self._contracts
    
    def add_contract(self, contract):   
        self._contracts.append(contract)

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)
        author.add_contract(self)  # Add contract to author's contracts list
        book.add_contract(self) # Add contract to books's contracts list

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

    @classmethod   
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if date == contract.date]
