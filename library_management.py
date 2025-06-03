from book import Book

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book Copies")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            try:
                year = int(input("Enter publication year: "))
                copies = int(input("Enter number of copies: "))
            except ValueError:
                print("Invalid year or copies input.")
                continue

            book = Book(title, author, year, copies)
            book.save_to_db()
            print("Book added successfully!")

        elif choice == '2':
            books = Book.list_books()
            print("\nList of Books:")
            print("ID | Title | Author | Year | Copies")
            for b in books:
                print(f"{b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]}")

        elif choice == '3':
            try:
                book_id = int(input("Enter book ID to update copies: "))
                new_copies = int(input("Enter new number of copies: "))
                Book.update_copies(book_id, new_copies)
                print("Book copies updated.")
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            try:
                book_id = int(input("Enter book ID to delete: "))
                Book.delete_book(book_id)
                print("Book deleted.")
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
