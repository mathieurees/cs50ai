from heredity import load_data, check_one_gene, joint_probability

class TestJointProbabilityAndItsUtils():

    def test_check_one_gene_no_listed_parents(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Lily"}, {"James"}, {"James"})
        excepted = 0.03
        assert actual == excepted

    def test_check_one_gene_parent_has_two_genes(self):
        people = load_data("data/family0.csv")
        actual = check_one_gene(people, {"Harry"}, {"James"}, {"James"})
        excepted = 0.9802
        assert actual == excepted