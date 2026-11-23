# write a menu driven program that keeps track of books in a library.s, search for a book by title, and delete a book by title. Each book should have a title, author, and publication year.```python
class Book:
    
    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = 0
        
        
    def read(self):
        self.title = input("Enter the title of the book: ")
        self.author = input("Enter the author of the book: ")
        self.price = float(input("Enter the price of the book: "))
        
        
    def display(self):
        print("title:", self.title)        
        print("author:", self.author)        
        print("price:", self.price)
        
        
        
my_books = []
ch="y"

while (ch=="y"):
    print("""1. Add a book\n2.display books""")                
    
    choice=int(input("enter the choice"))
    if(choice==1):
        book=Book()
        book.read()
        
        my_books.append(book)
    elif(choice==2):
        for i in my_books:
            i.display()
            
    else:
        print("invalid choice")
        
    ch=input("do you want to continue(y/n): ")
    
 
print("bye")


                
    