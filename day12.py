# Create a class called Circle with the following attributes:
# radius (float)
# The class should also have a class attribute called pi which is a constant value of 3.14159.

# Implement the following methods:
# get_radius: Returns the radius of the circle.
# get_area: Returns the area of the circle, calculated as the product of pi and the square of the radius.
# get_circumference: Returns the circumference of the circle, calculated as 2 times pi times the radius.

# Additionally, implement a class method called compare_circles that takes two circle objects as parameters and compares their areas. The method should return 1 if the first circle has a larger area, -1 if the second circle has a larger area, and 0 if both circles have the same area.


# Create two instances of the Circle class, each with different radii. Print out the details of each circle, including the radius, area, and circumference.
# Test the class method compare_circles by comparing the two circles and printing the result.
# Note: The value of pi should be accessible both through the class attribute (Circle.pi) and through instances (circle_instance.pi).

class Circle:
    pi = 3.14159
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def get_area(self):
        return (self.radius ** 2) * Circle.pi
    
    def get_circumference(self):
        return 2 * Circle.pi * self.radius

    @classmethod
    def compare_circles(cls, circle1, circle2):
        area1 = circle1.get_area()
        area2 = circle2.get_area()

        if(area1 > area2):
            return 1
        elif(area1 < area2):
            return -1
        elif(area1 == area2):
            return 0

    


    


a = Circle(5)
print(a.pi)
print(a.get_area())    
print(a.get_circumference())    

circle1 = Circle(6)
circle2 = Circle(6)

result = Circle.compare_circles(circle1, circle2)
print(result)