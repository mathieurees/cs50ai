from heredity import *
from math import isclose

PEOPLE = load_data("data/family0.csv")

class TestHasParents:

    def test_with_parents(self):
        assert has_parents(PEOPLE, "Harry")
    
    def test_without_parents(self):
        assert not has_parents(PEOPLE, "James")

class TestGeneProbNoParents:

    def test_one_gene(self):
        assert gene_prob_no_parents(PEOPLE, 'Lily', 1) == 0.03

    def test_two_genes(self):
        assert gene_prob_no_parents(PEOPLE, 'Lily', 2) == 0.01
