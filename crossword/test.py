import pytest
from copy import copy
from crossword import *
from generate import *

@pytest.fixture
def test_game():
    return CrosswordCreator(Crossword("./data/structure0.txt",
                                       "./data/words0.txt"))

class TestEnforceNodeConistency:

    def test_function_alters_domains(self, test_game):
        initial_domains = copy(test_game.domains)
        test_game.enforce_node_consistency()
        new_domains = copy(test_game.domains)
        assert initial_domains != new_domains