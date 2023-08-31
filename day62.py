# -------------------- Encapsulation ---------------------


#  ---------------------------- Question --------------------------

# Explain the difference between private, protected, and public access specifiers in encapsulation. Provide an example of each.


# Private  = __
# Protected  = _
# Public = 

class Animal:
    def __init__(self, name, species, color) -> None:
        self.__name = name #private
        self._name = name #protected
        self.name = name #public
    
    def get_name(self):
        return self.__name

    def set_name(self, newname):
        self.__name = newname

cat = Animal('cat-x', 'xspecies', 'black')
print(f"The name of the animal is : {cat.name}, and this a public attribute") #public
print(f"The name of the animal is : {cat._name}, and this a protected attribute") #protected
print(f"The name of the animal is : {cat.get_name()} and this a private attribute accessed via get method") #running the private attribute with the help of get method

#print(f"The name of the animal is : {cat.__name}, and this a private attribute") #private - it wont be running because it cannot be accessed directly outside the class however to access it outside the class we use get or set methods

cat.set_name('cat - y')
print(f"The name of the animal is : {cat.get_name()} and this a private attribute accessed via get method") 


