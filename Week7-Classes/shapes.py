import math


class Polygon:
    # class level, static, attributes
    number_of_polygons = 0
    # constructor
    def __init__(self, number_of_sides):
        Polygon.number_of_polygons += 1
        self._number_of_sides = number_of_sides
        self._sides_lengths = [0] * number_of_sides

    def set_side_length(self, length, side_index):
        if length <= 0:
            raise ValueError("invalid length")
        self._sides_lengths[side_index] = length

    def get_perimeter(self):
        return sum(self._sides_lengths)

    def get_number_of_sides(self):
        return self._number_of_sides

    def get_side_length(self, side_index):
        return self._sides_lengths[side_index]

    def get_side_lengths(self):
        # creates a new list, but not a deep copy
        return self._sides_lengths[:]

    # inherits from polygon
class Rectangle(Polygon):

    def __init__(self, length, width):
        super().__init__(4)
        self.set_width(width)
        self.set_length(length)

    def set_side_length(self, length, side_index):
        if side_index % 2 == 0:
            super().set_side_length(length, 0)
            super().set_side_length(length, 2)
        else:
            super().set_side_length(length, 1)
            super().set_side_length(length, 3)

    def set_length(self, length):
        self.set_side_length(length, 0)

    def set_width(self, width):
        self.set_side_length(width, 1)

    def get_area(self):
        return self._sides_lengths[0] * self._sides_lengths[1]


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    def set_width(self, width):
        super().set_length(width)
        super().set_width(width)

    def set_side_length(self, length, side_index):
        self.set_length(length)

class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter
                         *(semi_perimeter-self._sides_lengths[0])
                         *(semi_perimeter-self._sides_lengths[1])
                         *(semi_perimeter-self._sides_lengths[2])
                         )