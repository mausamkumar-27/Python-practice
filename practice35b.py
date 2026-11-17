class Book:
    def __init__(self,title,author,price,genre="Fiction"):
        self.title=title
        self.author=author
        self.price=price
        self.genre=genre
    def book_details(self):
        print(f"Title:{self.title} | Author:{self.author} | Price:{self.price} | Genre:{self.genre}")
b1=Book("Deep Work","James Watt",199,"Self Help")
b2=Book("Atomic Habits","James Clear",399)
b1.book_details()
b2.book_details()