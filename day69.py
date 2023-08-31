# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Design a class called "Restaurant" with private attributes "menu" (a dictionary of menu items) and "name". Implement methods to add items to the menu, remove items from the menu, and display the menu. Demonstrate encapsulation by creating a Restaurant object, adding and removing menu items, and displaying the menu.


class Restaurant:
    def __init__(self, name) -> None:
        self.__menu = {} #private attribute 
        self.__name = name #private attribute 
    
    def add_items(self, item, price):
        # we will be adding the item as the key and the price as the value of items dictionary in the restaurant class
        self.__menu[item] = price
    
    def remove_items(self, item):
        if(item in self.__menu):
            del self.__menu[item]
        print(f'The {item} is not there in the menu')

    
    def display_menu(self):
        print(f"The menu in the {self.__name}")
        if(len(self.__menu)>0):
            for item, price in self.__menu.items():
                print(f"{item} : {price}")
        else:
            print('ALERT: There is not item in the menu')

a = Restaurant('delicious food')
(a.display_menu())
print()
print()
a.add_items('pasta', 200)
a.add_items('maggie', 80)
(a.display_menu())
print()
print()
a.remove_items('pasta')
(a.display_menu())





