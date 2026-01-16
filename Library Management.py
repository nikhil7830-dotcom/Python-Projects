import os
BOOKS_FILE = "books.txt"
# Create file if not exists
if not os.path.exists(BOOKS_FILE):
    open(BOOKS_FILE, "w").close()
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    status = "Available"
    with open(BOOKS_FILE, "a") as file:
        file.write(f"{book_id},{title},{author},{status}\n")
    print("Book added successfully")
def view_books():
    print("\n Library Books:")
    with open(BOOKS_FILE, "r") as file:
        for line in file:
            book_id, title, author, status = line.strip().split(",")
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    updated_books = []
    with open(BOOKS_FILE, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == book_id and data[3] == "Available":
                data[3] = "Issued"
                print("Book issued successfully")
            updated_books.append(",".join(data))
    with open(BOOKS_FILE, "w") as file:
        file.write("\n".join(updated_books))
def return_book():
    book_id = input("Enter Book ID to return: ")
    updated_books = []
    with open(BOOKS_FILE, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == book_id and data[3] == "Issued":
                data[3] = "Available"
                print(" Book returned successfully")
            updated_books.append(",".join(data))
    with open(BOOKS_FILE, "w") as file:
        file.write("\n".join(updated_books))
def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("👋 Exiting system")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
