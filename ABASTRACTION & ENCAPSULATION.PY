#ABSTRACTION AND ENCAPSULATION IN PYTHON


class library:
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print('avaliable books')
        for book in self.books:
            print(bool)
    def borrow_books(self,borrow_books):
        if borrow_books in self.books:
            print('get your book')
            self.books.remove(borrow_books)
        else:
            print('book not avaliable')
    def receive_book(self,receive_book):
        print('book received')
        self.books.append(receive_book)

books = ['c++','java','python']
o=library(books)
msg='''
   1.display book
   2.borrow book
   3.receive book
'''
while True:
    print(msg)
    ch=int(input('Enter your choice : '))
    if ch==1:
        o.list_books()
    elif ch==2:
        book=input('Enter book name to borrow : ')
        o.borrow_books(book)
    elif ch==3:
        book=input('Enter book name to return : ')
        o.receive_book(book)
    else:
        print('thank you ')
        exit()

