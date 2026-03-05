from minesweeper import Sentence, Minesweeper

class TestSentence():

    def test_known_mines_when_no_mines_known(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        assert sentence.known_mines() == set()
    
    def test_known_mines_when_all_mines_known(self):
        sentence = Sentence([(0,1), (0,2)], 2)
        assert sentence.known_mines() == set(((0,1), (0,2)))