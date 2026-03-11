from pagerank import DAMPING, SAMPLES, crawl, transition_model, sample_pagerank, check_convergence, rank_page, iterate_pagerank
import math

class TestTransitionModel():
    
    def test_simple_model(self):
        test_corpus = crawl("corpus0")
        current_page = "1.html"
        expected = {
            "1.html": 0.0375,
            "2.html": 0.8875,
            "3.html": 0.0375,
            "4.html": 0.0375,
        }
        actual = transition_model(test_corpus, current_page, DAMPING)
        sum_probs = 0
        for page in actual:
            actual_prob = actual[page]
            sum_probs += actual_prob
            expected_prob = expected[page]
            assert math.isclose(actual_prob, expected_prob)
        assert math.isclose(sum_probs, 1)

    def test_no_links_to_page(self):
        test_corpus = crawl("corpus2")
        current_page = "recursion.html"
        actual = transition_model(test_corpus, current_page, DAMPING)
        expected = {
            "ai.html": 0.125,
            "algorithms.html": 0.125,
            "c.html": 0.125,
            "inference.html": 0.125,
            "logic.html": 0.125,
            "programming.html": 0.125, 
            "python.html": 0.125,
            "recursion.html": 0.125
        }
        sum_probs = 0
        for page in actual:
            actual_prob = actual[page]
            sum_probs += actual_prob
            expected_prob = expected[page]
            assert math.isclose(actual_prob, expected_prob)
        assert math.isclose(sum_probs, 1)

class TestSamplePagerank():

    def test_correct_highest_value(self):
        test_corpus = crawl("corpus0")
        rankings = sample_pagerank(test_corpus, DAMPING, SAMPLES)
        highest_rank = rankings.pop("2.html")
        assert all(rankings[page] < highest_rank for page in rankings)

    def test_values_sum_to_one(self):
        test_corpus = crawl("corpus0")
        rankings = sample_pagerank(test_corpus, DAMPING, SAMPLES)
        value_sum = 0
        for page in rankings:
            value_sum += rankings[page]
        assert math.isclose(value_sum, 1)

class TestCheckConvergence():

    def test_returns_false_given_no_convergence(self):
        assert not check_convergence({"Test1": 0.5}, {"Test1": 1.5}, 0.5)

    def test_returns_true_given_convergence(self):
        assert check_convergence({"Test1": 0.5}, {"Test1": 0.9}, 0.5)

class TestRankPage():

    def test_no_randomness(self):
        page = "Test1"
        old_ranking = {
            "Test1": 0.25,
            "Test2": 0.25,
            "Test3": 0.25,
            "Test4": 0.25,
        }
        damping = 1
        corpus = {
            "Test1": ["Test2"],
            "Test2": ["Test3"],
            "Test3": ["Test4"],
            "Test4": ["Test1"],
        }
        assert rank_page(page, old_ranking, damping, corpus) == 0.25

    def test_all_randomness(self):
        page = "Test1"
        old_ranking = {
            "Test1": 0.25,
            "Test2": 0.25,
            "Test3": 0.25,
            "Test4": 0.25,
        }
        damping = 0
        corpus = {
            "Test1": ["Test2"],
            "Test2": ["Test3"],
            "Test3": ["Test4"],
            "Test4": ["Test1"],
        }
        assert rank_page(page, old_ranking, damping, corpus) == 0.25

class TestIteratePagerank():

    def test_correct_highest_value(self):
        test_corpus = crawl("corpus0")
        rankings = iterate_pagerank(test_corpus, DAMPING)
        highest_rank = rankings.pop("2.html")
        assert all(rankings[page] < highest_rank for page in rankings)
