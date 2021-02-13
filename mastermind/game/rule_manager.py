
class Rule_manager:
    
    def __init__(self):
        self.hint = '****'
        self.num_turn = 0
    
    
    def _get_hint(self, number, guess):
        """
        check if the guessed number is in the number
        return hint: "****"
        """
        list_num = []
        list_hint = list(self.hint)
        for i in range(4):
            list_num.append(number[i:i+1])
        
        for i in range(4):
            for j in range(4):
                if guess[i:i+1] == list_num[j]:
                    if i == j:
                        list_hint[i] = 'x'
                    else:
                        list_hint[i] = 'o'
        hint = ""
        for i in list_hint:
            hint += i
        return hint

    def _game_over(self, number, guess):
        """
        If the guessed number is correct, return False
        """

        if guess == number:
            return False
        
        return True

    def get_current(self, players):
        """
        return current player
        """
        return players[self.num_turn] 

    def next_player(self):
        """
        return 0 or 1, it will determine the turn
        """
        self.num_turn = (self.num_turn + 1 ) % 2
        return self.num_turn

