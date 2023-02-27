#Write a python program to calculate the perimeter of a triangle

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

side1 = float(input("Length of side 1: "))
side2 = float(input("Length of side 2: "))
side3 = float(input("Length of side 3: "))

triangle = Triangle(side1, side2, side3)
perimeter = triangle.calculate_perimeter()
print(f"The perimeter of the triangle is: {perimeter}")
