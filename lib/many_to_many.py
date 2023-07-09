class Author:
    all = []
    def __init__(self, name):
        self.name=name
        Author.all.append(self) 
    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    def books(self):
        return[contract.book for contract in Contract.all if contract.author==self]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)       
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
class Book:
    all = []
    def __init__(self, title):
        self.title=title
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book==self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book==self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.set_author(author)     
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        Contract.all.append(self)
    def set_author(self, author):
        if isinstance(author, Author):
            self.author = author
        else: raise Exception
    def set_book(self, book):
        if isinstance(book, Book):
            self.book=book
        else: raise Exception
    def set_date(self, date):
        if isinstance(date, str):
            self.date=date
        else: raise Exception
    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self.royalties = royalties
        else: raise Exception
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda d: d.date)