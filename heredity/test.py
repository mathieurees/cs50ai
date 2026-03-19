from heredity import load_data, check_one_gene, check_two_genes, joint_probability
from math import isclose

class TestCheckOneGene():

    def test_check_one_gene_no_listed_parents(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Lily"}, {"James"})
        excepted = 0.03
        assert isclose(actual, excepted)

    def test_check_one_gene_one_parent_has_two_genes(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Harry"}, {"James"})
        excepted = 0.9802
        assert isclose(actual, excepted)

    def test_check_one_gene_both_parents_have_two_genes(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Harry"}, {"James", "Lily"})
        excepted = 0.0198
        assert isclose(actual, excepted)

    def test_check_one_gene_one_parent_has_one_gene(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Harry", "James"}, set())
        excepted = 0.014705999999999999
        assert isclose(actual, excepted)


class TestCheckTwoGenes():

    def test_check_two_genes_no_listed_parents(self):
        people = load_data("data/family0.csv")
        actual = check_two_genes(people, {"Lily"}, {"James"})
        excepted = 0.01
        assert isclose(actual, excepted)
