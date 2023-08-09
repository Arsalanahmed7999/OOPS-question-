# Create two parent classes, "Shape" and "Color", with attributes and methods specific to each class, such as "calculate_area" in "Shape" and "set_color" in "Color".

# Create a child class called "ColoredShape" that inherits from both "Shape" and "Color". Implement a method called "display_info" in the "ColoredShape" class that calls the methods from both parent classes to calculate the area and set the color. Create an instance of the "ColoredShape" class and call the "display_info" method.

class Shape:
    def calculate_area(self):
        print('We are calculating area')


class Color:
    def set_color(self):
        print('We are setting the color')

class ColoredShape(Shape, Color): #name(parent1, parent2, ...)
    def display_info(self):
        self.calculate_area()
        self.set_color()

a = ColoredShape()
(a.display_info())
