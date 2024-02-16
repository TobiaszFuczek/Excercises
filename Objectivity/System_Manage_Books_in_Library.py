class Books:
    def __init__(self, book_id, title, author):
        self.book_id= book_id
        self.title= title
        self.author= author

class Library:
    def __init__(self):
        self.books_on= []
        self.books_checked_out= []
    def check_book(self, book_id, title):
        for book in self.books_on:
            if book.book_id == book_id:
                print(f"{title} is available to rent")
                return
        print(f"{title} is not available to rent")

    def rent(self, book_id, title):
        for book in self.books_on:
            if book.book_id == book_id:
                self.books_checked_out.append(book)
                self.books_on.remove(book)
                print(f"Your Book {title} has been hired")
                return
        print(f"The Book {title} ({book_id}) is not available")

    def donate(self, book):
        self.books_on.append(book)
        print(f"{book.title} ({book.book_id}) has been donated to Library")

    def return_book(self, book_id, title):
        for book in self.books_checked_out:
            if book.book_id == book_id:
                self.books_checked_out.remove(book)
                self.books_on.append(book)
                print(f"Thank you for returning {title}")
                return
        print(f"We do not have a record of {title} being checked out")



book1 = Books(book_id=1, title="Harry Potter and the Philosopher's Stone", author="J.K. Rowling")
book2 = Books(book_id=2, title="The Great Gatsby", author="F. Scott Fitzgerald")
book3 = Books(book_id=3, title="To Kill a Mockingbird", author="Harper Lee")

library = Library()

library.donate(book1)
library.donate(book2)
library.donate(book3)

library.check_book(book_id=2, title="The Great Gatsby")

library.rent(book_id=2, title="The Great Gatsby")

library.check_book(book_id=2, title="The Great Gatsby")

library.return_book(book_id=2, title="The Great Gatsby")

library.check_book(book_id=2, title="The Great Gatsby")

