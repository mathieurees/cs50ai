import pytest
from degrees import shortest_path

def test_returns_correct_type():
    possible_list = shortest_path('x', 'y')
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