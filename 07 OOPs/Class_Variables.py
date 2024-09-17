# Assignment 2 Book repersentation in library using class variables
class Book:
    title = ""
    author = ""
    year = ""
    available = True
    number_of_books = 0
    __pages= 100

    def __init__(self, title1, author1, year1, avai1=True):
        self.title= title1
        self.author = author1
        self.year = year1
        self.available = avai1

    @staticmethod
    def staticMessage():
        print("Books are man's best friend ")
        print(Book.__pages)
    def displayInfo(self):
        Book.number_of_books += 1
        print(f'Book Info \n Title : {self.title} \n Author : {self.author} \n year : {self.year} \n Is Availabe : {self.available} \n and books quantity is : {Book.number_of_books}')
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' is borrowed by you")
        else:
            print("Book not available")
    def return_book(self):
        if self.available==False:
            self.available = True
            print(f"The book '{self.title}' is returned by you")
        else:
            print("Book is already available")

book1 = Book("My Life My Rule","Jayesh C.","2020")
book2 = Book("Drishyam ","Ajay D.", "2014")
book1.displayInfo()
book2.displayInfo()
Book.staticMessage()

book1.borrow_book()
book1.displayInfo()
book1.return_book()