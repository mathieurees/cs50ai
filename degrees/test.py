import pytest, os
from degrees import shortest_path, load_data

load_data(os.getcwd() + "/small")   # navigate to degrees subdirectory first

def test_returns_correct_type():
    possible_list = shortest_path("102", "102")
    is_correct = isinstance(possible_list, list) 
    if is_correct:
        for possible_tuple in possible_list:
            if not isinstance(possible_tuple, tuple): 
                is_correct = False
                break
            if len(possible_tuple) != 2:
                is_correct = False
                break
            for possible_string in possible_tuple:
                if not isinstance(possible_string, str):
                    is_correct = False
                    break
    assert is_correct or possible_list is None

class TestReturnsNoneWhenNoInputHasNoFilms():
 
    def test_returns_none_when_source_has_no_films(self):
        output = shortest_path("914612", "102")
        assert output is None

    def test_returns_none_when_target_has_no_films(self):
        output = shortest_path("102", "914612")
        assert output is None
    
    def test_returns_none_when_neither_has_films(self):
        output = shortest_path("102", "102")
        assert output is None

class TestReturnsShortestLengthOnePath():

    def test_correct_when_inputs_different(self):
        output = shortest_path("1597", "144")
        assert output == [("93779", "144")] # source 1597 starred in movie 93779 with person 144

    def test_order_irrelevant(self):
        output = shortest_path("144", "1597")
        assert output == [("93779", "1597")]

class TestReturnsShortestLengthTwoPath():

    def test_correct_when_inputs_different(self):
        output = shortest_path("102", "163")
        assert output == [("104257", "129"), ("95953", "163")] 

    def test_order_irrelevant(self):
        output = shortest_path("163", "102")
        assert output == [("95953", "129"), ("104257", "102")]
