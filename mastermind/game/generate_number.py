import random


class GenerateNumber:

    def __init__(self):
        """
        The constructor method.
        """
        self._number = 0
        self.guess = ''
        self.random_number = 0
        # self.guess1 = '----'
        # self.guess2 = '----'
        self.guesses = []

    def set_number(self):
        """
        The set_number method sets a number range and returns a random choice in
        that range.
        """
        # self._number = (1000, 9999)
        self.random_number = str(random.randint(1000, 10000))
        return self.random_number

    def get_number(self):
        """
        The get_number method gets the value from set_number and returns the value
        and sends it to screen.
        """
        return self.random_number

    def get_guess(self, player):
        """
        The get_guess method prompts the user to input their guess and returns that
        value to screen.
        """
        print(f"{player}'s turn:")
        guess = str(input("What is your gguess? "))
        print()
        return guess
        # self.guess1 = input(int(f'{self.player1} What is your guess? '))
        # self.guess2 = input(int(f'{self.player2} What is your guess? '))

        # return self.guess1 and self.guess2

    def guess_call_1(self):
        """
        This method just returns the value of guess 1.
        """
        return self.guess1

    def guess_call_2(self):
        """
        This method just returns the value of guess 2.
        """
        return self.guess2
