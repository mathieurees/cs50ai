from minesweeper import Sentence, MinesweeperAI

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

    def test_mark_mine_relevant_cell(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        sentence.mark_mine((0,2))
        assert sentence.cells == set(((0,1),))
        assert sentence.count == 0

    def test_mark_mine_irrelevant_cell(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        sentence.mark_mine((0,5))
        assert sentence.cells == set(((0,1), (0,2)))
        assert sentence.count == 1

    def test_mark_safe_relevant_cell(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        sentence.mark_safe((0,2))
        assert sentence.cells == set(((0,1),))
        assert sentence.count == 1

    def test_mark_safe_irrelevant_cell(self):
        sentence = Sentence([(0,1), (0,2)], 1)
        sentence.mark_safe((0,5))
        assert sentence.cells == set(((0,1), (0,2)))
        assert sentence.count == 1

class TestAddKnowledge():

    def test_mark_cell_as_made_move(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0,1), 3)
        assert ai.moves_made == set(((0,1),))

    def test_mark_cell_as_safe_cell(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0,1), 3)
        assert ai.safes == set(((0,1),))

    def test_updates_knowledge_give_safe_cell(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(0,1), (0,2)], 1))
        ai.add_knowledge((0,1), 2)
        assert ai.knowledge[0] == Sentence([(0,2)], 1)

    def test_adds_new_sentence_to_knowledge(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0, 0), 2)
        ai.add_knowledge((7, 7), 3)
        nearby_cells_top_left = [(0,1), (1,0), (1,1)]
        nearby_cells_btm_right = [(6,7), (6,6), (7,6)]
        top_left_sentence = Sentence(nearby_cells_top_left, 2) 
        btm_right_sentence = Sentence(nearby_cells_btm_right, 3) 
        assert ai.knowledge[0] == top_left_sentence
        assert ai.knowledge[1] == btm_right_sentence