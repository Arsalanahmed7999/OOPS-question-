# -------------------- Encapsulation ---------------------

#  -------------------- Question --------------------------

# Create a class called "MenuItem" with private attributes "name", "price", and "ingredients" (a list of ingredient names). Implement methods to modify the price and display the details of a menu item. 



class Menuitem:
    def __init__(self, name, price, ingredients) -> None:

        # self.name = name #public attribute

        self.__name = name #private attibute
        self.__price = price #private attribute
        self.__ingredients = ingredients #private attribute
    
    # def get_name(self):
    #     return self.__name
    
    # def get_price(self):
    #     return self.__price

    def modify_price(self, newprice):
        self.__price = newprice
    
    def display_details(self):
        return (f"Name: {self.__name}, Price: {self.__price}, Ingredients: {self.__ingredients}")
    


pasta = Menuitem('pasta', 100, ['pasta', 'water', 'salt', 'pepper'])
# print(pasta.get_name())
# print(pasta.get_price())
print(pasta.display_details())

pasta.modify_price(150)
# print(pasta.get_price())
print(pasta.display_details())

