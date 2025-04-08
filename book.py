class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.is_open = False
        self.current_page = 0

    def open_book(self):
        self.is_open = True
        print(f"{self.title} is now open.")

    def close_book(self):
        self.is_open = False
        print(f"{self.title} is now closed.")

    def turn_page(self):
        if self.is_open:
            if self.current_page < self.pages - 1:
                self.current_page += 1
                print(f"Turned to page {self.current_page + 1}.")
            else:
                print("You've reached the end of the book.")
        else:
            print("Please open the book first.")

    def __str__(self): # For a nice string representation of the object
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"



class eBook(Book): # Inherits from Book
    def __init__(self, title, author, genre, pages, file_format):
        super().__init__(title, author, genre, pages) # Call the parent class's constructor
        self.file_format = file_format
        self.font_size = 12 # Encapsulation: font_size is specific to eBook

    def change_font_size(self, new_size):
        self.font_size = new_size
        print(f"Font size changed to {self.font_size}.")

    def turn_page(self): # Polymorphism: Overriding the turn_page method
        if self.is_open:
            if self.current_page < self.pages - 1:
                self.current_page += 1
                print(f"Swiped to page {self.current_page + 1}.") # Different message
            else:
                print("You've reached the end of the eBook.")
        else:
            print("Please open the eBook first.")


# Example usage:
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 310)
print(book1)
book1.open_book()
book1.turn_page()
book1.turn_page()
book1.close_book()


ebook1 = eBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction", 224, "PDF")
print(ebook1)
ebook1.open_book()
ebook1.turn_page()
ebook1.change_font_size(14)


