import pytest
from copy import deepcopy
from crossword import *
from generate import *


@pytest.fixture
def test_game_0():
    """
    Returns tuple containing simple game, and its variables.

    Simple game has only two variables in its crossword. One variable 
    is 3 accross, beginning at (0,1). The other is 5 down, begining at 
    (0,1) also. So their point of intersection is (0,0). 

    Accross is the accross word variable. Down is the down word variable.

    Default filepath to words test file is "./data/testwords0.txt".
    """
    def _test_game_0(*test_words_file):
        test_struct = "./data/teststructure0.txt"
        test_words = test_words_file or "./data/testwords0.txt"
        test_game = CrosswordCreator(Crossword(test_struct, test_words))
        across = Variable(0, 1, "across", 3)
        down = Variable(0, 1, "down", 5)
        return test_game, across, down
    return _test_game_0

class TestEnforceNodeConsistency:

    def test_alters_domains(self, test_game_0):
        simple_game = test_game_0()[0]
        initial_domains = deepcopy(simple_game.domains)
        simple_game.enforce_node_consistency()
        new_domains = simple_game.domains
        assert initial_domains != new_domains

    def test_removes_word_when_too_large(self, test_game_0):
        simple_game = test_game_0()[0]
        across = test_game_0()[1]
        simple_game.enforce_node_consistency()
        assert "seven" not in simple_game.domains[across]

    def test_removes_word_when_too_small(self, test_game_0):
        simple_game = test_game_0()[0]
        down = test_game_0()[2]
        simple_game.enforce_node_consistency()
        assert "six" not in simple_game.domains[down]
    


        