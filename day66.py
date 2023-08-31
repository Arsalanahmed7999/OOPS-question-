# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Create a class called "Library" with private attributes "books" (a dictionary of book titles and authors) and "members" (a list of member names). Implement methods to add books to the library, check out a book, and display the list of books and members. Demonstrate encapsulation by creating a library object, adding books, checking out books, and displaying information about the library's contents.

class Library:
    def __init__(self) -> None:
        self.__books = {}   #this is a private attribute
        self.__members = [] #this is a private attribute
    
    def add_books(self, title, author):
        #title is a key, author is value {key: value}
        self.__books[title] = author

    def checkout(self, title):
        if title in self.__books:
            del self.__books[title]
            return True
        else:
            return False  
    
    def get_books(self):
        return self.__books
    
    def get_members(self):
        return self.__members
    
    def display_books(self):
        print('The book in the library')
        for title, author in self.__books.items():
            print (f"Title : {title}, Author: {author}")
    
    def display_members(self):
        print('The Members in the Library')
        for member in self.__members:
            print(f"Members : {member}")
    
    def add_members(self, member):
        self.__members.append(member)

    
a = Library()
# print(a.get_books())
a.add_books('title2', 'author2')
a.add_books('titlexyz', 'william')
# print(a.get_books())
(a.display_books())


# adding members to the list
print()
print()
print()
(a.display_members())
a.add_members('Arslan')
a.add_members('Ahmed')
a.add_members('rohit')
(a.display_members())



