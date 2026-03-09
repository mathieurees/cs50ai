from minesweeper import Sentence, MinesweeperAI
import pytest

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

    def test_adds_new_sentence_to_knowledge(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0, 0), 2)
        ai.add_knowledge((7, 7), 1)
        nearby_cells_top_left = [(0,1), (1,0), (1,1)]
        nearby_cells_btm_right = [(6,7), (6,6), (7,6)]
        top_left_sentence = Sentence(nearby_cells_top_left, 2) 
        btm_right_sentence = Sentence(nearby_cells_btm_right, 1) 
        assert ai.knowledge[0] == top_left_sentence
        assert ai.knowledge[1] == btm_right_sentence

    def test_infers_new_safe_cell(self):
        ai = MinesweeperAI()
        ai.mines = set(((1,1),))
        ai.add_knowledge((0,0), 1)
        assert (0, 1) in ai.safes
        assert (1, 0) in ai.safes

    def test_infers_new_mine_trivial(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0,0), 3)
        assert set(((0,1), (1,0), (1,1))) == ai.mines

    def test_infers_new_mine_from_safe(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(1,1), (2,2), (3,3),], 2))
        ai.add_knowledge((0,0), 0)
        assert set(((2,2), (3,3))) == ai.mines

    def test_infers_new_safes_trivial(self):
        ai = MinesweeperAI()
        ai.add_knowledge((0,0), 0)
        assert set(((0,0),(0,1), (1,0), (1,1))) == ai.safes
    
    def test_infers_new_safes_from_safe(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(1,1), (2,2), (3,3),], 1))
        ai.add_knowledge((0,0), 3)
        assert set(((0,0), (2,2), (3,3))) == ai.safes
    
    def test_makes_subset_inference_given_new_knowledge(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(0,1), (1,0), (1,1), (1,2), (1,3)], 4))
        ai.add_knowledge((0,0), 3)
        assert Sentence([(1,2), (1,3)], 1) in ai.knowledge
        
class TestMakeSafeMove():

    def test_returns_none_when_no_safe_move_known(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(0,1), (0,2)], 1))
        assert ai.make_safe_move() is None

    def test_returns_none_when_moves_allready_chosen(self):
        ai = MinesweeperAI()
        for i in range(8):
            for j in range(8):    
                ai.moves_made.add((i, j))
        ai.add_knowledge((0,1), 0)
        assert ai.make_safe_move() is None

    def test_returns_safe_move(self):
        ai = MinesweeperAI()
        ai.knowledge.append(Sentence([(0,1), (0,2), (0,3)], 1))
        ai.add_knowledge((0,0), 3)
        assert ai.make_safe_move() == (0,2)

class TestMakeRandomMove():
    
    def test_random_returns_none_when_no_viable_move(self):
        ai = MinesweeperAI()
        for i in range(8):
            for j in range(8):
                if i != j:
                    ai.moves_made.add((i, j))
                else:
                    ai.mines.add((i, j))
        assert ai.make_random_move() is None

    def test_random_returns_move_not_yet_made(self):
        ai = MinesweeperAI()
        for i in range(8):
            for j in range(8):
                if i != j:
                    ai.moves_made.add((i, j))
                else:
                    ai.mines.add((i, j))
        ai.moves_made.remove((0,1))
        assert ai.make_random_move() == (0,1)

    def test_random_returns_move_not_known_mine(self):
        ai = MinesweeperAI()
        for i in range(8):
            for j in range(8):
                if i != j:
                    ai.moves_made.add((i, j))
                else:
                    ai.mines.add((i, j))
        ai.mines.remove((0,0))
        assert ai.make_random_move() == (0,0)