class Library:
    def __init__(self,lists_of_books):
        self.books=lists_of_books
    def display_available_books(self):
        print("Books present in the library are : ")
        for books in self.books:
            print("\t"+books)
    def borrow_books(self,book_name):
        if book_name in self.books:
            print(f"you issued a book {book_name}....please keep it safe and make sure returned back within 10 days")
            self.books.remove(book_name)
            return True

        else:
            print("Book is either not available or  currently issued by someone else ....try it again after some days")
            return False
    
    def return_book(self,book_name):
        self.books.append(book_name)
        print("Thanks for returning the book....hope u enjoyed it..")
class Student:
    def request_book(self):
        self.book=input("Enter the name of the book u want to borrow : ")
        return self.book
    def return_book(self):
        self.book=input("Enter a book u want return : ")
        return self.book
if __name__ == '__main__':
    Ipeclibrary=Library(["c","python","algorithm","django","flask","javascript","\n","\t"])
    # Ipeclibrary.display_available_books()
    Student=Student()
    while True:
        welcomemsg='''\n***************WELCOME TO IPEC LIBRARY*******************
        PLEASE CHOOSE AN OPTION :
        1. LIST OF ALL THE BOOKS
        2. REQUEST OF BOOKS
        3. RETURN OF BOOKS
        4. EXIT THE LIBRARY'''
        print(welcomemsg)
        a=int(input("Enter your choice : "))
        if a==1:
            Ipeclibrary.display_available_books()
        elif a==2:
            Ipeclibrary.borrow_books(Student.request_book())
        elif a==3:
            Ipeclibrary.return_book(Student.return_book())
        elif a==4:
            print("THANKS !!!   for using this library...Hope u enjoyed...")
            exit()

        else:
            print("Invalid choice")