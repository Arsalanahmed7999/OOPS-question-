#1. Create a class called "Library" with attributes books and members. The "books" attribute should be a list that stores the names of books available in the library. The "members" attribute should be a list that stores the names of library members. Implement methods to add a book to the library, remove a book from the library, add a member to the library, and remove a member from the library.

class Library:
    def __init__(self, books, members) -> None:
        self.books = books
        self.members = members
    
    def add_book(self, new_book):
        self.books.append(new_book)
        print('The book has been added successfully')

    def remove_book(self, new_book):
        if(new_book in self.books):
            self.books.remove(new_book)
            print('The book has been removed successfully')
        else:
            print (f'The {new_book} is not in the list')

    def add_member(self, new_member):
        self.members.append(new_member)
        print('The book has been added successfully')

    def remove_member(self, new_member):
        if(new_member in self.members):
            self.members.remove(new_member)
            print('The book has been removed successfully')
        else:
            print (f'The {new_member} is not in the list')

abc = Library(['book1', 'book2'], ['Arsalan', 'Ahmed'])
print(abc.books)
abc.add_book('bookxyz')
print(abc.books)
abc.remove_book('bookxyz')
print(abc.books)
abc.remove_book('bookxyz')
print(abc.books)
print(abc.members)
abc.add_member('Raju')
print(abc.members)
# books = ['book1', 'books2', 'book3']