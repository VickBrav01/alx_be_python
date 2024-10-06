# class Book:
#     def __init__(self, title, author, is_checked_out):
#         self.title = title
#         self.author = author
#         self.__is_checked_out = is_checked_out

# class Library(Book):
#     def __init__(self, title, author, is_checked_out, _book):
#         self.__book = _book
#         super().__init__(title, author, is_checked_out)

#     def add_book(self):

#         pass

#     def check_out_book(self, title):
#         pass

#     def return_book(self, title):
#         pass

#     def list_available_books(self):
#         pass

# library_management.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book is already checked out

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book wasn't checked out

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempts to check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Attempts to return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"'{book.title}' by {book.author}")
        else:
            print("No books are currently available.")
