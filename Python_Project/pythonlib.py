# class Book:
#     def __init__(self, title, author, year, isbn, copies=1):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.isbn = isbn
#         self.available_copies = copies

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Available Copies: {self.available_copies}"

#     def update_details(self, title=None, author=None, year=None, isbn=None):
#         if title: self.title = title
#         if author: self.author = author
#         if year: self.year = year
#         if isbn: self.isbn = isbn

#     def add_copies(self, copies):
#         self.available_copies += copies

#     def remove_copy(self):
#         if self.available_copies > 0:
#             self.available_copies -= 1

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Book '{book.title}' added to the library.")

#     def display_books(self):
#         if len(self.books) == 0:
#             print("No books in the library.")
#         else:
#             for book in self.books:
#                 print(book)

#     def search_book(self, title=None, author=None, isbn=None):
#         found_books = [book for book in self.books if
#                        (title and title.lower() in book.title.lower()) or
#                        (author and author.lower() in book.author.lower()) or
#                        (isbn and isbn == book.isbn)]
        
#         if not found_books:
#             print("No books found.")
#         else:
#             for book in found_books:
#                 print(book)

#     def check_out_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn and book.available_copies > 0:
#                 book.remove_copy()
#                 print(f"You have checked out '{book.title}'.")
#                 return
#         print("Book not available for checkout or doesn't exist.")

#     def return_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 book.add_copies(1)
#                 print(f"Book '{book.title}' has been returned.")
#                 return
#         print("This book is not checked out or doesn't exist.")

#     def update_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 title = input("Enter new title (or leave blank to keep unchanged): ")
#                 author = input("Enter new author (or leave blank to keep unchanged): ")
#                 year = input("Enter new year of publication (or leave blank to keep unchanged): ")
#                 isbn_new = input("Enter new ISBN (or leave blank to keep unchanged): ")
#                 book.update_details(
#                     title=title if title else None,
#                     author=author if author else None,
#                     year=year if year else None,
#                     isbn=isbn_new if isbn_new else None
#                 )
#                 print(f"Book '{book.title}' updated successfully.")
#                 return
#         print("Book not found.")

#     def remove_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 self.books.remove(book)
#                 print(f"Book '{book.title}' has been removed from the library.")
#                 return
#         print("Book not found.")

# def main():
#     library = Library()

#     while True:
#         print("\nLibrary Management System")
#         print("1. Add Book")
#         print("2. Display Books")
#         print("3. Search for Book")
#         print("4. Checkout Book")
#         print("5. Return Book")
#         print("6. Update Book Details")
#         print("7. Remove Book")
#         print("8. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             title = input("Enter book title: ")
#             author = input("Enter author name: ")
#             year = input("Enter year of publication: ")
#             isbn = input("Enter ISBN: ")
#             copies = int(input("Enter number of copies: "))
#             book = Book(title, author, year, isbn, copies)
#             library.add_book(book)

#         elif choice == '2':
#             library.display_books()

#         elif choice == '3':
#             search_choice = input("Search by (1) Title, (2) Author, (3) ISBN, or (4) All: ")
#             if search_choice == '1':
#                 title = input("Enter title to search: ")
#                 library.search_book(title=title)
#             elif search_choice == '2':
#                 author = input("Enter author to search: ")
#                 library.search_book(author=author)
#             elif search_choice == '3':
#                 isbn = input("Enter ISBN to search: ")
#                 library.search_book(isbn=isbn)
#             elif search_choice == '4':
#                 title = input("Enter title to search: ")
#                 author = input("Enter author to search: ")
#                 isbn = input("Enter ISBN to search: ")
#                 library.search_book(title=title, author=author, isbn=isbn)

#         elif choice == '4':
#             isbn = input("Enter ISBN of book to checkout: ")
#             library.check_out_book(isbn)

#         elif choice == '5':
#             isbn = input("Enter ISBN of book to return: ")
#             library.return_book(isbn)

#         elif choice == '6':
#             isbn = input("Enter ISBN of book to update: ")
#             library.update_book(isbn)

#         elif choice == '7':
#             isbn = input("Enter ISBN of book to remove: ")
#             library.remove_book(isbn)

#         elif choice == '8':
#             print("Exiting the system...")
#             break

#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}"

class Book:
    def __init__(self, title, author, year, isbn, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available_copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Available Copies: {self.available_copies}"

    def update_details(self, title=None, author=None, year=None, isbn=None):
        if title: self.title = title
        if author: self.author = author
        if year: self.year = year
        if isbn: self.isbn = isbn

    def add_copies(self, copies):
        self.available_copies += copies

    def remove_copy(self):
        if self.available_copies > 0:
            self.available_copies -= 1

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, title=None, author=None, isbn=None):
        found_books = [book for book in self.books if
                       (title and title.lower() in book.title.lower()) or
                       (author and author.lower() in book.author.lower()) or
                       (isbn and isbn == book.isbn)]
        
        if not found_books:
            print("No books found.")
        else:
            for book in found_books:
                print(book)

    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available_copies > 0:
                book.remove_copy()
                print(f"You have checked out '{book.title}'.")
                return
        print("Book not available for checkout or doesn't exist.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.add_copies(1)
                print(f"Book '{book.title}' has been returned.")
                return
        print("This book is not checked out or doesn't exist.")

    def update_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                title = input("Enter new title (or leave blank to keep unchanged): ")
                author = input("Enter new author (or leave blank to keep unchanged): ")
                year = input("Enter new year of publication (or leave blank to keep unchanged): ")
                isbn_new = input("Enter new ISBN (or leave blank to keep unchanged): ")
                book.update_details(
                    title=title if title else None,
                    author=author if author else None,
                    year=year if year else None,
                    isbn=isbn_new if isbn_new else None
                )
                print(f"Book '{book.title}' updated successfully.")
                return
        print("Book not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                return
        print("Book not found.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' removed from the library.")
                return
        print("Member not found.")

    def list_members(self):
        if len(self.members) == 0:
            print("No members in the library.")
        else:
            for member in self.members:
                print(member)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search for Book")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Update Book Details")
        print("7. Remove Book")
        print("8. Add Member")
        print("9. Remove Member")
        print("10. List Members")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            isbn = input("Enter ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, year, isbn, copies)
            library.add_book(book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            search_choice = input("Search by (1) Title, (2) Author, (3) ISBN, or (4) All: ")
            if search_choice == '1':
                title = input("Enter title to search: ")
                library.search_book(title=title)
            elif search_choice == '2':
                author = input("Enter author to search: ")
                library.search_book(author=author)
            elif search_choice == '3':
                isbn = input("Enter ISBN to search: ")
                library.search_book(isbn=isbn)
            elif search_choice == '4':
                title = input("Enter title to search: ")
                author = input("Enter author to search: ")
                isbn = input("Enter ISBN to search: ")
                library.search_book(title=title, author=author, isbn=isbn)

        elif choice == '4':
            isbn = input("Enter ISBN of book to checkout: ")
            library.check_out_book(isbn)

        elif choice == '5':
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == '6':
            isbn = input("Enter ISBN of book to update: ")
            library.update_book(isbn)

        elif choice == '7':
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)

        elif choice == '8':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            member = Member(member_id, name, email)
            library.add_member(member)

        elif choice == '9':
            member_id = input("Enter member ID to remove: ")
            library.remove_member(member_id)

        elif choice == '10':
            library.list_members()

        elif choice == '11':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
