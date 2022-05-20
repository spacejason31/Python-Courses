class Polygon():
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
        """A class to describe several common attributes of shapes"""

    @property
    def num_sides(self):
        self.num_sides = len(self.side_lengths)
        return num_sides

    @staticmethod
    def __str__(self):
        print('Polygon with %s sides' % self.sides)

class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__([height, width, height, width])
        self.height = height
        self.width = width

    def calc_area(self):
        self.area = self.height*self.width
        return self.area

    @property
    def calc_perimeter(self):
        self.perimeter = sum(self.side_lengths)
        return self.perimeter

shape1 = Rectangle(5, 12)
shape1.calc_area()
shape1.calc_perimeter

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

shape2 = Square(5)
print(shape2.calc_perimeter, shape2.calc_area())
