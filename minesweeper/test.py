from minesweeper import Sentence, Minesweeper

class TestSentence():

    def test_known_mines_when_no_mines_known(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        assert sentence.known_mines() == set()
    
    def test_known_mines_when_all_mines_known(self):
        sentence = Sentence([(0,1), (0,2)], 2)
        assert sentence.known_mines() == set(((0,1), (0,2)))

    def test_known_safes_when_no_safes_known(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        assert sentence.known_safes() == set()
    
    def test_known_safes_when_all_safes_known(self):
        sentence = Sentence([(0,1), (0,2)], 0)
        assert sentence.known_safes() == set(((0,1), (0,2)))