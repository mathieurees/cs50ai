from heredity import *
from math import isclose

PEOPLE = load_data("data/family0.csv")

class TestHasParents:

    def test_with_parents(self):
        assert has_parents(PEOPLE, "Harry")
    
    def test_without_parents(self):
        assert not has_parents(PEOPLE, "James")