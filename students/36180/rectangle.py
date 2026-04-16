class Rectangle:
    
    def __init__(self, width, height):
        # Storing width and height as properties
        self.width = width
        self.height = height

    
    def area(self):
        # Returns width multiplied by height
        return self.width * self.height

    
    def perimeter(self):
        # Returns the perimeter: 2 * (width + height)
        return 2 * (self.width + self.height)


r1 = Rectangle(5, 3)
print(f"Area: {r1.area()}")
print(f"Perimeter: {r1.perimeter()}")