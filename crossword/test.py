import pytest
from copy import deepcopy
from crossword import *
from generate import *


@pytest.fixture
def test_game_0():
    """
    Returns tuple containing simple game, and its variables.

    Test game has only two variables in its crossword. One variable 
    is 3 accross, beginning at (0,1). The other is 5 down, begining at 
    (0,1) also. So their point of intersection is (0,0). 

    Accross is the accross word variable. Down is the down word variable.

    Test words are 'six' and 'seven'.
    """
    test_struct = "./data/teststructure0.txt"
    test_words = "./data/testwords0.txt"
    test_game = CrosswordCreator(Crossword(test_struct, test_words))
    across = Variable(0, 1, "across", 3)
    down = Variable(0, 1, "down", 5)
    return test_game, across, down


class TestEnforceNodeConsistency:

    def test_alters_domains(self, test_game_0):
        test_game = test_game_0[0]
        initial_domains = deepcopy(test_game.domains)
        test_game.enforce_node_consistency()
        new_domains = test_game.domains
        assert initial_domains != new_domains

    def test_removes_word_when_too_large(self, test_game_0):
        test = test_game_0
        test_game = test[0]
        across = test[1]
        test_game.enforce_node_consistency()
        assert "SEVEN" not in test_game.domains[across]

    def test_removes_word_when_too_small(self, test_game_0):
        test = test_game_0
        test_game = test[0]
        down = test[2]
        test_game.enforce_node_consistency()
        assert "SIX" not in test_game.domains[down]
    

class TestRevise:

    def test_does_not_remove_given_arc_consistency(self, test_game_0):
        test = test_game_0
        test_game = test[0]
        across = test[1]
        down = test[2]
        test_game.domains[down].add("TWO")
        assert not test_game.revise(across, down)
        assert test_game.domains[across] == {"SIX", "SEVEN"}
        assert test_game.domains[down] == {"SIX", "SEVEN", "TWO"}

    def test_does_remove_given_arc_inconsistency(self, test_game_0):
        test = test_game_0("./data/testwords1.txt")
        test_game = test[0]
        across = test[1]
        down = test[2]
        test_game.domains[down] = {"TWO"}
        assert test_game.revise(across, down)
        assert test_game.domains[across] == set()
        assert test_game.domains[down] == {"TWO"}