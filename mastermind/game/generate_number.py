import random
from game.roster import Roster


class GenerateNumber:

    def __init__(self):
        """
        The constructor method.
        """
        self._number = 0
        self.guess = ''
        self.random_number = 0

    def set_number(self):
        """
        The set_number method sets a number range and returns a random choice in
        that range.
        """
        self._number = (1000, 9999)
        self.random_number = random.choice(self._number)
        return self.random_number
        pass

    def get_number(self):
        """
        The get_number method gets the value from set_number and returns the value
        and sends it to screen.
        """
        return self.random_number
        pass

    def get_guess(self):
        """
        The get_guess method prompts the user to input their guess and returns that
        value to screen.
        """
        guess = input(int(f'{self.player1} What is your guess? '))
        guess_2 = input(int(f'{self.player2} What is your guess? '))

        return guess and guess_2
        pass

    pass
