
class Guess:

    def __init__(self, random):
        self._number = random.randint(1, 10)
        self._guesses = 0

    def guess(self, number):
        self._guesses += 1
        if number == self._number:
            return True
        return False

    def get_number_of_guesses(self):
        return self._number