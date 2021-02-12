class Board:

    def __init__(self):
        """
        The constructor of the Board class
        """
        self._spacer = '--------------------\n'
        self._p1_guess = '----'
        self._p2_guess = '----'


        pass

    def to_string(self, p1_name, p2_name):
        """
        Formats the content to a string so that it can be displayed on the screen without issue
        Takes the names from the Roster class as arguments
        :return: string
        """
        string = self._spacer + "Player " + p1_name + ': ' + p2_name + ', '
        string +=

        pass

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