from game.board import Board
from game.rule_manager import Rule_manager
from game.roster import Roster
from game.generate_number import GenerateNumber

class Director:
    
    def __init__(self):
        self._board = Board()
        self._generate_number = GenerateNumber()
        self._roster = Roster()
        self._rule_manager = Rule_manager()

    def start_game(self):
        pass

    def _prepare_game(self):
        pass
    
    def _get_inputs(self):
        pass

    def _do_updates(sefl):
        pass

    def _do_outputs(self):
        pass