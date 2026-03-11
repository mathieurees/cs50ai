from pagerank import DAMPING, SAMPLES, crawl, transition_model, sample_pagerank
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