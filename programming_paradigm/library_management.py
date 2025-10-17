class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self):
        self._is_checked_out = True
        
    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self):  # it is necessary because we can't access the ___is_checked_out outside this class
        return not (self._is_checked_out)

class Library:
    def __init__(self):
        self._books = []      # private attribute of name _book
    
    
    def Add_Book(self, book):
        self._books.append(book)
        
    def Check_out_Book(self, title): 
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
            
    def Return_Book(self, title):
        for book in self._books:
            if book.title == title and not(book.is_available()):
                book.return_book()
        
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")