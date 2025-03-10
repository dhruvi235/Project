import json
from datetime import datetime, timedelta

class Book:
    COLORS = {
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "cyan": "\033[36m",
        "green": "\033[32m",
        "red": "\033[31m",
        "magenta": "\033[35m",
        "reset": "\033[0m"
    }

    def __init__(self, title, author, isbn, copies):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = int(isbn)
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = None
        self.due_date = None

    def display_details(self):
        status = f"{self.COLORS['green']}Available ✅{self.COLORS['reset']}" if self.available_copies > 0 else f"{self.COLORS['red']}Checked Out ❌{self.COLORS['reset']}"
        borrower_info = f"{self.COLORS['red']}🔹 Borrowed By: {self.borrowed_by}, Due Date: {self.due_date}{self.COLORS['reset']}" if self.borrowed_by else ""
        print(f"\n{self.COLORS['blue']}📖 Title: {self.title}{self.COLORS['reset']}\n"
              f"{self.COLORS['yellow']}✍️  Author: {self.author}{self.COLORS['reset']}\n"
              f"{self.COLORS['cyan']}🔢 ISBN: {self.isbn}{self.COLORS['reset']}\n"
              f"{self.COLORS['cyan']}📌 Status: {status}{self.COLORS['reset']}\n"
              f"{self.COLORS['magenta']}📦 Total Copies: {self.total_copies}{self.COLORS['reset']}\n"
              f"{self.COLORS['green']}📖 Available Copies: {self.available_copies}{self.COLORS['reset']}\n"
              f"{borrower_info}\n")

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.isbn},{book.total_copies},{book.available_copies},{book.borrowed_by},{book.due_date}\n")

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    title, author, isbn, total_copies, available_copies, borrowed_by, due_date = line.strip().split(",")
                    book = Book(title, author, int(isbn), int(total_copies))
                    book.available_copies = int(available_copies)
                    book.borrowed_by = borrowed_by if borrowed_by != "None" else None
                    book.due_date = due_date if due_date != "None" else None
                    self.books.append(book)
        except FileNotFoundError:
            print("No existing books data found. Starting fresh.")

    def add_book(self, title, author, isbn, copies):
     while True:
        author = input(f"{Book.COLORS['cyan']}Enter author name: {Book.COLORS['reset']}").strip()
        
        if all(word.isalpha() for word in author.split()):
            break 

        print(f"{Book.COLORS['red']}❌ Invalid author name! Please enter only alphabets and spaces.{Book.COLORS['reset']}")

        self.books.append(Book(title, author, int(isbn), int(copies)))
        self.save_books()
        print(f"\n{Book.COLORS['blue']}📚 Book '{title.title()}' added successfully!{Book.COLORS['reset']}")

    def search_book(self, keyword):
        keyword = keyword.lower()
        found_books = [book for book in self.books if keyword in book.title.lower() or keyword in book.author.lower() or keyword in str(book.isbn)]
        if found_books:
            print(f"\n{Book.COLORS['cyan']}🔍 Search Results:{Book.COLORS['reset']}")
            for book in found_books:
                book.display_details()
        else:
            print(f"\n{Book.COLORS['red']}❌ No matching books found.{Book.COLORS['reset']}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_copies > 0:
                member_name = input(f"{Book.COLORS['cyan']}Enter your name: {Book.COLORS['reset']}").strip().title()
                book.available_copies -= 1
                book.borrowed_by = member_name
                book.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                self.save_books()
                print(f"\n{Book.COLORS['yellow']}🛒 '{book.title}' has been borrowed successfully by {member_name}! Due Date: {book.due_date}{Book.COLORS['reset']}")
                return
        print(f"\n{Book.COLORS['red']}❌ Book not available or not found.{Book.COLORS['reset']}")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_copies < book.total_copies:
                book.available_copies += 1
                book.borrowed_by = None
                book.due_date = None
                self.save_books()
                print(f"\n{Book.COLORS['green']}🔄 '{book.title}' has been returned successfully!{Book.COLORS['reset']}")
                return
        print(f"\n{Book.COLORS['red']}❌ Book not found or all copies are already returned.{Book.COLORS['reset']}")

    def display_books(self):
        if not self.books:
            print(f"\n{Book.COLORS['red']}📭 No books in the library.{Book.COLORS['reset']}")
            return
        print(f"\n{Book.COLORS['cyan']}📚 Library Collection:{Book.COLORS['reset']}")
        for book in self.books:
            book.display_details()

library = Library()
while True:
    print(f"\n{Book.COLORS['cyan']}📚 Library Management System{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}1️⃣  Add Book{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}2️⃣  Search Book{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}3️⃣  Display Books{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}4️⃣  Borrow Book{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}5️⃣  Return Book{Book.COLORS['reset']}")
    print(f"{Book.COLORS['blue']}6️⃣  Exit{Book.COLORS['reset']}")

    choice = input(f"\n{Book.COLORS['yellow']}Enter your choice: {Book.COLORS['reset']}").strip()

    if choice == "1":
        title = input(f"{Book.COLORS['cyan']}Enter book title: {Book.COLORS['reset']}")
        author = input(f"{Book.COLORS['cyan']}Enter author name: {Book.COLORS['reset']}")
        isbn = input(f"{Book.COLORS['cyan']}Enter ISBN number: {Book.COLORS['reset']}")
        copies = input(f"{Book.COLORS['cyan']}Enter number of copies: {Book.COLORS['reset']}")
        library.add_book(title, author, isbn, copies)
    
    elif choice == "2":
        keyword = input(f"{Book.COLORS['cyan']}Enter search keyword: {Book.COLORS['reset']}")
        library.search_book(keyword)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        title = input(f"{Book.COLORS['cyan']}Enter book title to borrow: {Book.COLORS['reset']}")
        library.borrow_book(title)

    elif choice == "5":
        title = input(f"{Book.COLORS['cyan']}Enter book title to return: {Book.COLORS['reset']}")
        library.return_book(title)

    elif choice == "6":
        print(f"{Book.COLORS['red']}Thank you for using the Library Management System! 📚{Book.COLORS['reset']}")
        break  # Exit the loop

    else:
        print(f"{Book.COLORS['red']}❌ Invalid choice! Please enter a valid option (1-6).{Book.COLORS['reset']}")
