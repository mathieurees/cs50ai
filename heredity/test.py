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
        assert gene_prob_no_parents(1) == 0.03

    def test_two_genes(self):
        assert gene_prob_no_parents(2) == 0.01

class TestGeneProbWithParents:

    def test_one_gene_one_parent_having_two_genes(self):
        expected = 0.9802
        actual = gene_prob_with_parents(PEOPLE, "Harry", {"Harry"}, {"James"}, 1)
        assert isclose(expected, actual)

    def test_one_gene_two_parents_having_two_genes(self):
        expected = 0.0198
        actual = gene_prob_with_parents(PEOPLE, "Harry", {"Harry"}, {"James", "Lily"}, 1)
        assert isclose(expected, actual)

    def test_one_gene_one_parent_having_one_gene(self):
        expected = 0.5
        actual = gene_prob_with_parents(PEOPLE, "Harry", {"Harry", "James"}, {}, 1)
        assert isclose(expected, actual)

    def test_two_genes_two_parents_having_two_genes(self):
        expected = 0.9801
        actual = gene_prob_with_parents(PEOPLE, "Harry", {}, {"Harry", "James", "Lily"}, 2)
        assert isclose(expected, actual)

    def test_no_genes_two_parents_having_no_genes(self):
        expected = 0.9801
        actual = gene_prob_with_parents(PEOPLE, "Harry", {}, {}, 0)
        assert isclose(expected, actual)
          
    