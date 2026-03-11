from pagerank import DAMPING, crawl, transition_model
import math

def test_transition_model():
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
        assert  math.isclose(actual_prob, expected_prob)
    assert math.isclose(sum_probs, 1)
