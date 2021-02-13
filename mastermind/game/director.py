from game.board import Board
from game.rule_manager import Rule_manager
from game.roster import Roster
from game.generate_number import GenerateNumber
from game.screen import Screen

class Director:
    
    def __init__(self):
        self._board = Board()
        self._generate_number = GenerateNumber()
        self._roster = Roster()
        self._rule_manager = Rule_manager()
        self._screen = Screen()
        self.keep_playing = True

    def start_game(self):
        self._prepare_game()
        while self.keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        # self.number = self._generate_number.set_number()
        self.number = "6888"
        print(self.number)
        self.players = self._roster.get_name()
        self.hints = ["****", "****"]
        self.board = self._board.to_string(self.players, self.hints)
        self._screen.write(self.board)
        
    def _get_inputs(self):
        #self.board = self._board.to_string(self.players, self.hints)
        self.player = self._rule_manager.get_current(self.players)
        self.guess = self._generate_number.get_guess(self.player)

    def _do_updates(self):
        num = (self._rule_manager.next_player() - 1)
        guess = self._board.get_guess(self.guess, num)
        self.hints[num] =self._rule_manager._get_hint(self.number, guess)
        self.board = self._board.to_string(self.players, self.hints)
        self.keep_playing = self._rule_manager._game_over(self.number, guess)


    def _do_outputs(self):
        if not self.keep_playing:
            self._screen.write(f"{self.player} won!")
        else:
            self._screen.write(self.board)