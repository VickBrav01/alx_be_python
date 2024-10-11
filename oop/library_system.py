class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        self.file_size = file_size
        super().__init__(title, author)
        
    def __str__(self):
        return f"EBook: {self.title} {self.author} File Size: {self.file_size}KB"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        super().__init__(title, author)
        
    def __str__(self):
        return f"PrintBook: {self.title} {self.author} Page Count: {self.page_count}"
        
class Library:
    books = []
    
    def add_book(self, book):
        Library.books.append(book)
    
    @classmethod
    def list_books(cls):
        for book in cls.books:
            print(book)
    