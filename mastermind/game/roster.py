

class Roster:

    def __init__(self):
        """
        The constructor method.
        """

        self._players = []
        # self.player1 = ''
        # self.player2 = ''

    def get_name(self):
        """
        The get_name method simply asks the players to input their names
        and then returns that value to screen.
        """
        player1 = input('Enter a name for player 1: ')
        self._players.append(player1)
        player2 = input('Enter a name for player 2: ')
        self._players.append(player2)
        print()

        return self._players

        # self.player1 = self._player1 = input('Player 1, what is your name? ')
        # self.player2 = self._player2 = input('Player 2, what is your name? ')

        # return self.player1 and self.player2

    def get_player_1(self):
        """
        This method just gets the value from player 1 and returns it.
        """
        return self.player1

    def get_player_2(self):
        """
        This method gets the value from player 2 and returns it.
        """
        return self.player2
