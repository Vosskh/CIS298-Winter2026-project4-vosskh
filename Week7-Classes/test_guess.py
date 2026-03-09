from unittest import TestCase
from guess import Guess


class FakeRandom:

    @staticmethod
    def randint(a, b):
        return 5

class TestGuess(TestCase):
    def test_guess(self):
        # Arrange
        guessing_game = Guess(FakeRandom)
        expected_guesses = 1

        # act
        result = guessing_game.guess(5)
        actual_number_of_guesses = 1

        # assert
        self.assertTrue(result)
        self.assertEqual(expected_guesses, actual_number_of_guesses)
