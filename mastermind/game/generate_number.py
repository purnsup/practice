import random
from game.roster import Roster


class GenerateNumber:

    def __init__(self):
        """
        The constructor method.
        """
        # self._generate_number(self) = ''
        self.number = (0, 9999)
        self.guess = ''

    def _generate_number(self):
        """
        The generate_number method is an encapsulated class that simply creates
        a random number and returns it.
        """
        self.num = random.choice(self.number)
        return self.num
        pass

    def get_number(self):
        """
        The get_number method calls the generate_number method's return value
        and sends it to screen.
        """

        # generate_number = self._generate_number(self)
        # return generate_number

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
