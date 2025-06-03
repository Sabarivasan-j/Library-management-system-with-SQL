from db_connection import get_connection

class Book:
    def __init__(self, title, author, year, copies):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Books (title, author, year, copies) VALUES (?, ?, ?, ?)",
            (self.title, self.author, self.year, self.copies)
        )
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def update_copies(book_id, new_copies):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Books SET copies = ? WHERE id = ?",
            (new_copies, book_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_book(book_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def list_books():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()
        conn.close()
        return rows
