from shapes import Rectangle
from unittest import TestCase


class TestRectangle(TestCase):
    def test_set_side_length(self):
        # AAA

        # Arrange - setup the variables we need
        rectangle = Rectangle(1,1)
        expected_length = 5
        expected_width = 10

        # Act - call the code we're testing
        rectangle.set_side_length(expected_length, 0)
        rectangle.set_side_length(expected_width, 1)
        actual_side_0 = rectangle.get_side_length(0)
        actual_side_1 =  rectangle.get_side_length(1)
        actual_side_2 = rectangle.get_side_length(2)
        actual_side_3 = rectangle.get_side_length(3)

        # Assert - did we get what we expected
        self.assertEqual(expected_length, actual_side_0)
        self.assertEqual(expected_length, actual_side_2)
        self.assertEqual(expected_width, actual_side_1)
        self.assertEqual(expected_width, actual_side_3)


    def test_set_length(self):
        # Arrange - setup the variables we need
        rectangle = Rectangle(1, 1)
        expected_length = 5

        # Act - call the code we're testing
        rectangle.set_length(expected_length)
        actual_side_0 = rectangle.get_side_length(0)
        actual_side_2 = rectangle.get_side_length(2)

        # Assert - did we get what we expected
        self.assertEqual(expected_length, actual_side_0)
        self.assertEqual(expected_length, actual_side_2)

    def test_set_width(self):
        # Arrange - setup the variables we need
        rectangle = Rectangle(1, 1)
        expected_width = 10

        # Act - call the code we're testing
        rectangle.set_width(expected_width)
        actual_side_1 = rectangle.get_side_length(1)
        actual_side_3 = rectangle.get_side_length(3)

        # Assert - did we get what we expected
        self.assertEqual(expected_width, actual_side_1)
        self.assertEqual(expected_width, actual_side_3)

    def test_get_area(self):
        # Arrange - setup the variables we need
        rectangle = Rectangle(4, 8)
        expected_area = 31

        # act
        actual_area = rectangle.get_area()

        # assert
        self.assertEqual(expected_area, actual_area)
