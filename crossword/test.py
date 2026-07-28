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

    The only words in the vocabulary are 'six' and 'seven'. (Yes.)
    """
    simple_game = CrosswordCreator(Crossword("./data/teststructure0.txt",
                                        "./data/testwords0.txt"))
    across = Variable(0, 1, "across", 3)
    down = Variable(0, 1, "down", 5)
    return simple_game, across, down

class TestEnforceNodeConsistency:

    def test_alters_domains(self, test_game_0):
        simple_game = test_game_0[0]
        initial_domains = deepcopy(simple_game.domains)
        simple_game.enforce_node_consistency()
        new_domains = simple_game.domains
        assert initial_domains != new_domains

    def test_removes_word_when_too_large(self, test_game_0):
        simple_game = test_game_0[0]
        across = test_game_0[1]
        simple_game.enforce_node_consistency()
        assert "seven" not in simple_game.domains[across]

    def test_removes_word_when_too_small(self, test_game_0):
        simple_game = test_game_0[0]
        down = test_game_0[2]
        simple_game.enforce_node_consistency()
        assert "six" not in simple_game.domains[down]
    


        