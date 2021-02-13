class Board:

    def __init__(self):
        """
        The constructor of the Board class
        """
        self._spacer = '--------------------\n'
        # self._p1_guess = '----'
        # self._p2_guess = '----'
        self._guesses = ["----", "----"]


        pass

    def to_string(self, players, hints):
        """
        Formats the content to a string so that it can be displayed on the screen without issue
        Takes the names from the Roster class as arguments
        :return: string
        """
        text = self._spacer
        for i in range(2):
            text += f"Player {players[i]}: {self._guesses[i]}, {hints[i]}\n"
        text += '--------------------'
        return text
        # string = self._spacer + "Player " + p1_name + ': ' + p2_name + ', '
        # string +=

        # pass

    def get_guess(self, guess, num):
        self._guesses[num] = guess
        return self._guesses[num]

    def print_guesses(self):
        """
        ?
        :return:
        """
        pass

    def print_num_condition(self):
        """
        ?
        :return:
        """
        pass