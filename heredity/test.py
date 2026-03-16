from heredity import load_data, check_one_gene, joint_probability
import math

class TestJointProbabilityAndItsUtils():

    def test_check_one_gene_no_listed_parents(self):
        people = load_data('data/family0.csv')
        assert check_one_gene(people, "James") == 0.03
