import os
import json

# File to store the library
LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                content = file.read()
                if content.strip():  # Check if not empty
                    return json.loads(content)
            except json.JSONDecodeError:
                print("⚠️ Warning: Corrupted library file. Starting with an empty library.")
    return []


# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("✅ Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed successfully!\n")
            return
    print("⚠️ Book not found.\n")

# Search for books
def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter search term: ").lower()
    matches = []

    if choice == "1":
        matches = [b for b in library if query in b["title"].lower()]
    elif choice == "2":
        matches = [b for b in library if query in b["author"].lower()]

    if matches:
        print("🔍 Matching Books:")
        for i, b in enumerate(matches, 1):
            read_status = "Read" if b["read"] else "Unread"
            print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {read_status}")
    else:
        print("😕 No matches found.")
    print()

# Display all books
def display_books(library):
    if not library:
        print("📭 Your library is empty.\n")
        return
    print("📚 Your Library:")
    for i, b in enumerate(library, 1):
        read_status = "Read" if b["read"] else "Unread"
        print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {read_status}")
    print()

# Show statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("📊 No books to show stats for.\n")
        return
    read_count = sum(1 for b in library if b["read"])
    percent_read = (read_count / total) * 100
    print(f"📈 Total books: {total}")
    print(f"✅ Percentage read: {percent_read:.1f}%\n")

# Menu system
def menu():
    library = load_library()
    print("📖 Welcome to your Personal Library Manager!")

    while True:
        print(""" 
Menu
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
