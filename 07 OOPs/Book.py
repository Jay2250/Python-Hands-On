# Assignment 1 Book repersentation in library
class Book:
    title = ""
    author = ""
    year = ""
    available = True

    def __init__(self, title1, author1, year1, avai1=True):
        self.title= title1
        self.author = author1
        self.year = year1
        self.available = avai1
    def displayInfo(self):
        print(f'Book Info \n Title : {self.title} \n Author : {self.author} \n year : {self.year} \n Is Availabe : {self.available}')
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

book1.borrow_book()
book1.displayInfo()
book1.return_book()

