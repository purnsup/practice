import random


class Roster:

    def __init__(self):
        """
        The constructor method.
        """
        self.player1 = ''
        self.player2 = ''
        pass

    def get_name(self):
        """
        The get_name method simply asks the players to input their names
        and then returns that value to screen.
        """
        self.player1 = input('Player 1, what is your name? ')
        self.player2 = input('Player 2 what is your name? ')

        return self.player1 and self.player2
        pass

    pass
