# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Design a class called "User" with private attributes "username", "email", and "friends" (a list of friend usernames). Implement methods to add friends, remove friends, and display user information. Demonstrate encapsulation by creating a User object, adding and removing friends, and displaying user details.

class User:
    def __init__(self, username, email) -> None:
        self.__username = username #private attribute
        # self.username = username #public attribute
        self.__email = email #private attribute
        self.__friends = [] #private attribute
    
    def add_user(self, newuser):
        self.__friends.append(newuser)
    
    def remove_user(self, user):
        # We will check whether the user is inside the friends list or not before removign it
        if(user in self.__friends):
            self.__friends.remove(user)
        else:
            print(f'{user} not found inside the friends list')
    
    def display_info(self):
        return (f"Username: {self.__username}\nEmail:{self.__email}\nFriends List : {self.__friends}")
    

ahmed = User('ahmed', 'ahmed@gmail.com')
print(ahmed.display_info())
print()
print()
ahmed.add_user('Arsalan')
print(ahmed.display_info())
print()
print()
ahmed.remove_user('Arsalan')
print(ahmed.display_info())
print()
print()
ahmed.remove_user('Arsalan')
print(ahmed.display_info())
