import pytest
from copy import deepcopy
from crossword import *
from generate import *

@pytest.fixture
def test_game():
    return CrosswordCreator(Crossword("./data/structure0.txt",
                                       "./data/words0.txt"))

class TestEnforceNodeConsistency:

    def test_alters_domains(self, test_game):
        initial_domains = deepcopy(test_game.domains)
        test_game.enforce_node_consistency()
        new_domains = test_game.domains
        assert initial_domains != new_domains

    def test_removes_word_when_too_large(self, test_game):
        test_game.enforce_node_consistency()
        for variable in test_game.domains:
            domain = test_game.domains[variable]
            if not domain:
                assert False
            assert all(
                len(value) <= variable.length for value in domain
            ) 

    def test_removes_word_when_too_small(self, test_game):
            test_game.enforce_node_consistency()
            for variable in test_game.domains:
                domain = test_game.domains[variable]
                if not domain:
                    assert False
                assert all(
                    len(value) >= variable.length for value in domain
                ) 
    
    

        