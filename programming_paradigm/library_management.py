class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self.___is_checked_out = False
        
    def check_out(self):
        self.___is_checked_out = True
        
    def return_book(self):
        self.___is_checked_out = False
    
    def is_available(self):  # it is necessary because we can't access the ___is_checked_out outside this class
        return not (self.___is_checked_out)

class Library:
    def __init__(self):
        self.___books = []      # private attribute of name _book
    
    
    def Add_book(self, book):
        self.___books.append(book)
        
    def Check_out_book(self, title): 
        for book in self.___books:
            if book.title == title and book.is_available():
                book.check_out()
            
    def Return_book(self, title):
        for book in self.___books:
            if book.title == title and not(book.is_available()):
                book.return_book()
        
    def list_available_books(self):
        for book in self.___books:
            if book.is_available():
                print(f"{book.title} by {book.author}")