from abc import ABC, abstractmethod
import math


# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete Subclasses
class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Side length must be positive.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Polymorphism
def calculate_total_properties(shapes):
    total_area = sum(shape.area() for shape in shapes)
    total_perimeter = sum(shape.perimeter() for shape in shapes)

    return total_area, total_perimeter


# User Interaction
def main():
    shapes = []

    while True:
        print("Select a shape to create:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Calculate total properties")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                radius = float(input("Enter the radius of the circle: "))
                if radius <= 0:
                    raise ValueError("The radius must be positive.")
                shapes.append(Circle(radius))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                width = float(input("Enter the width of the rectangle: "))
                height = float(input("Enter the height of the rectangle: "))
                if width <= 0 or height <= 0:
                    raise ValueError("Width and height must be positive.")
                shapes.append(Rectangle(width, height))
            except ValueError as e:
                print(f"Error {e}")
        elif choice == "3":
            try:
                side1 = float(input("Enter the length of side 1: "))
                side2 = float(input("Enter the length of side 2: "))
                side3 = float(input("Enter the length of side 3: "))
                if side1 <= 0 or side2 <= 0 or side3 <= 0:
                    raise ValueError("All lengths of sides must be positive.")
                shapes.append(Triangle(side1, side2, side3))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            if shapes:
                total_area, total_perimeter = calculate_total_properties(shapes)
                print(f"Total area: {total_area}")
                print(f"Total perimeter: {total_perimeter}")
            else:
                print("No shapes created yet.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


"""
1. Abstract Class (Shape):
- An abstract class is a class that cannot be instantiated on its own. 
Instead, it serves as a blueprint for other classes.
- In this case, Shape is an abstract class that defines the common 
interface for different shapes.
- It provides methods for calculating the area and perimeter of a shape, 
but these methods are left unimplemented (abstract).

2. ABC Module:
- The ABC module stands for Abstract Base Classes.
- It provides the necessary infrastructure for defining abstract base 
classes in Python.
- Abstract base classes can have abstract methods, which must be 
implemented by concrete subclasses.

3. @abstractmethod Decorator:
- The @abstractmethod decorator is used to mark methods as abstract within 
an abstract class.
- Abstract methods do not have an implementation in the abstract class but 
must be implemented by concrete subclasses.
- In this case, both area and perimeter methods are marked as abstract, 
indicating that any concrete subclass of Shape must provide implementations 
for these methods.


What is an abstract class?
 - An abstract class is the name for any class from 
 which you can instantiate an object.
 - Abstract classes must be redefined any time an object 
 is instantiated from them.
 - Abstract classes must inherit from concrete classes.
 - *An abstract class exists only so that other 
 "concrete" classes can inherit from the abstract class.*
"""
