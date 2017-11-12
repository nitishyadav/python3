#library 

class Library:
    def __init__(self, lostOfBooks):
        self.availableBooks = listOfBooks
        
    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
        
    def lendBook(self):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")
        
    def addBook(self):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank YOu!")
        
class Customer:
    def requestBook(self):
        Print("Enter the name of the book you would like to borrow:")
        self.book = input()
        return self.book
        
    def returnBook(self):
        Print("Enter the name of the book which you are returning:")
        self.book = input()
        return self.book
        
library = Library(['Think and Grow Rich','Who will cry when you Die','For one more Day'])
customer = Customer()  
print("Enter 1 to display the available books")
print("Enter 2 to request for a book")
print("Enter 3 to return a book")
print("Enter 4 to exit")      