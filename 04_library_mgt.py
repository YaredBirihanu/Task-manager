class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name}, Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from library.")
                return
        print("Book not found.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def list_books(self):
        return [str(book) for book in self.books]

    def list_patrons(self):
        return [str(patron) for patron in self.patrons]


class FrontendManager:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            print("\n--- Library Management System ---")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Register Patron")
            print("4. Borrow Book")
            print("5. Return Book")
            print("6. List All Books")
            print("7. List All Patrons")
            print("8. Search for a Book")
            print("9. Exit")
            choice = input("Choose an option (1-9): ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book = Book(title, author, isbn)
                self.library.add_book(book)

            elif choice == '2':
                isbn = input("Enter ISBN of the book to remove: ")
                self.library.remove_book(isbn)

            elif choice == '3':
                name = input("Enter patron name: ")
                patron = Patron(name)
                self.library.register_patron(patron)

            elif choice == '4':
                patron_name = input("Enter patron name: ")
                book_title = input("Enter book title to borrow: ")
                patron = next((p for p in self.library.patrons if p.name.lower() == patron_name.lower()), None)
                book = next((b for b in self.library.books if b.title.lower() == book_title.lower()), None)
                if patron and book:
                    patron.borrow_book(book)
                else:
                    print("Patron or book not found.")

            elif choice == '5':
                patron_name = input("Enter patron name: ")
                book_title = input("Enter book title to return: ")
                patron = next((p for p in self.library.patrons if p.name.lower() == patron_name.lower()), None)
                book = next((b for b in self.library.books if b.title.lower() == book_title.lower()), None)
                if patron and book:
                    patron.return_book(book)
                else:
                    print("Patron or book not found.")

            elif choice == '6':
                books = self.library.list_books()
                print("\nBooks in Library:")
                for book in books:
                    print(book)

            elif choice == '7':
                patrons = self.library.list_patrons()
                print("\nRegistered Patrons:")
                for patron in patrons:
                    print(patron)

            elif choice == '8':
                title = input("Enter book title to search: ")
                found_books = self.library.search_book(title)
                if found_books:
                    print("\nFound Books:")
                    for book in found_books:
                        print(book)
                else:
                    print("No books found.")

            elif choice == '9':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()