import os
import datetime

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = int(isbn)
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = None
        self.due_date = None

    def display_details(self):
        status = "Available" if self.available_copies > 0 else "Checked Out"
        borrower_info = f"Borrowed By: {self.borrowed_by}, Due Date: {self.due_date}" if self.borrowed_by else ""
        print(f"\nTitle: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nStatus: {status}\nTotal Copies: {self.total_copies}\nAvailable Copies: {self.available_copies}\n{borrower_info}\n")

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn, copies):
        try:
            if not author.replace(" ", "").isalpha() or not copies.isdigit() or not isbn.isdigit():
                raise ValueError("Invalid input! Author must be a valid string, ISBN and copies must be numbers.")
            new_book = Book(title, author, int(isbn), int(copies))
            self.books.append(new_book)
            self.save_books()
            print(f"\nBook '{title.title()}' added successfully! You can now borrow (4) or return (5) books.")
            return new_book
        except ValueError as e:
            print(f"\nError: {e}")

    def borrow_book(self, title, member_name):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_copies > 0:
                book.available_copies -= 1
                book.borrowed_by = member_name
                book.due_date = datetime.date.today() + datetime.timedelta(days=14)
                self.save_books()
                print(f"\n'{book.title}' has been borrowed successfully by {member_name}! Due Date: {book.due_date}")
                return
        print("\nBook not available or not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_copies < book.total_copies:
                book.available_copies += 1
                book.borrowed_by = None
                book.due_date = None
                self.save_books()
                print(f"\n'{book.title}' has been returned successfully!")
                return
        print("\nBook not found or all copies are already returned.")

    def display_books(self):
        if not self.books:
            print("\nNo books in the library.")
            return
        print("\nLibrary Collection:")
        for book in self.books:
            book.display_details()

    def advanced_filter(self, filter_type, filter_value):
        filter_value = filter_value.lower()
        if filter_type == "author":
            filtered_books = [book for book in self.books if book.author.lower() == filter_value]
        elif filter_type == "availability":
            filtered_books = [book for book in self.books if (filter_value == "available" and book.available_copies > 0) or (filter_value == "checked out" and book.available_copies == 0)]
        elif filter_type == "title":
            filtered_books = [book for book in self.books if filter_value in book.title.lower()]
        else:
            print("\nInvalid filter type. Choose 'author', 'availability', or 'title'.")
            return

        if filtered_books:
            print("\nFiltered Results:")
            for book in filtered_books:
                book.display_details()
        else:
            print("\nNo books match the given filter.")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.isbn},{book.total_copies},{book.available_copies},{book.borrowed_by},{book.due_date}\n")

    def load_books(self):
        if os.path.exists("books.txt") and os.path.getsize("books.txt") > 0:
            with open("books.txt", "r") as file:
                for line in file:
                    title, author, isbn, total_copies, available_copies, borrowed_by, due_date = line.strip().split(",")
                    book = Book(title, author, int(isbn), int(total_copies))
                    book.available_copies = int(available_copies)
                    book.borrowed_by = borrowed_by if borrowed_by != "None" else None
                    book.due_date = due_date if due_date != "None" else None
                    self.books.append(book)
        else:
            print("\nNo saved books found. Adding default books.")
            self.add_default_books()
            self.save_books()

    def add_default_books(self):
        default_books = [
            ("Python Programming", "John Doe", "123456789", "5"),
            ("Data Structures and Algorithms", "Jane Smith", "987654321", "3"),
            ("Artificial Intelligence", "Alan Turing", "192837465", "4"),
            ("Machine Learning Basics", "Andrew Ng", "564738291", "2"),
            ("Web Development with JavaScript", "Chris Evans", "847362915", "6"),
            ("Cyber Security Essentials", "Edward Snowden", "736291847", "5")
        ]
        for title, author, isbn, copies in default_books:
            self.add_book(title, author, isbn, copies)

# Menu
library = Library()
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Advanced Filtering")
    print("6. Exit")
    
    choice = input("\nEnter your choice: ").strip()
    
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number (only digits): ")
            copies = input("Enter number of copies: ")
            library.add_book(title, author, isbn, copies)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            title = input("Enter book title to borrow: ")
            member_name = input("Enter your name: ")
            library.borrow_book(title, member_name)
        elif choice == 4:
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == 5:
            filter_type = input("Filter by 'author', 'availability', or 'title': ").strip().lower()
            filter_value = input("Enter filter value: ").strip().lower()
            library.advanced_filter(filter_type, filter_value)
        elif choice == 6:
            print("\nThank you for using the Library Management System!")
            break
        else:
            print("\nInvalid choice, please try again.")
    else:
        print("\nInvalid input! Please enter a valid number.")