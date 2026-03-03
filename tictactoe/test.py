from tictactoe import initial_state, EMPTY, X, O, player, actions, result, winner, terminal, utility, minimax, find_min, find_max
import pytest

class TestPlayer():

    def test_player_returns_X_for_empty_board(self):
        assert player(initial_state()) == X

    def test_player_returns_X_for_nonempty_board(self):
        board = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        assert player(board) == X

    def test_player_returns_O_for_nonempty_board(self):
        board = [
            [X, EMPTY, O],
            [EMPTY, X, O],
            [EMPTY, X, EMPTY]
        ]
        assert player(board) == O

class TestActions():

    def test_action_returns_initial_state_given_initial_state(self):
        expected = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        assert expected == actions(initial_state())
    
    def test_action_handles_non_initial_state(self):
        board = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY]
        ]
        expected = [
            (0, 1), (1, 0), (1, 1), 
            (1, 2), (2, 0), (2, 2)
        ]
        assert expected == actions(board)

class TestResult():

    x_move_board = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ] 
    o_move_board = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY]
        ] 
    valid_action = (1, 2)
    invalid_action = (0, 2)

    def test_result_produces_correct_x_board(self):
        expected = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY]
        ] 
        assert expected == result(self.x_move_board, self.valid_action)

    def test_result_produces_correct_o_board(self):
        expected = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, O],
            [EMPTY, X, EMPTY]
        ] 
        assert expected == result(self.o_move_board, self.valid_action)

    def test_does_not_mutate_original_board(self):
        output = result(self.o_move_board, self.valid_action) 
        assert output is not self.o_move_board
        assert output != self.o_move_board 

    def test_result_raises_exception_for_incorrect_action(self):
        with pytest.raises(Exception):
            result(self.o_move_board, self.invalid_action)

class TestWinner():

    def test_horizontal_winner(self):
        x_wins = [
            [X, X, X],
            [O, O, X],
            [X, O, O]
        ]
        o_wins = [
            [O, O, O],
            [X, X, X],
            [O, X, EMPTY]
        ]
        assert X == winner(x_wins)
        assert O == winner(o_wins)

    def test_vertical_winner(self):
        x_wins = [
            [X, X, O],
            [X, O, X],
            [X, O, O]
        ]
        o_wins = [
            [X, O, O],
            [X, X, O],
            [EMPTY, X, O]
        ]
        assert X == winner(x_wins)
        assert O == winner(o_wins)

    def test_diagonal_winner(self):
        x_wins = [
            [X, X, O],
            [O, X, EMPTY],
            [X, O, X]
        ]
        o_wins = [
            [X, X, O],
            [X, O, X],
            [O, EMPTY, O]
        ]
        assert X == winner(x_wins)
        assert O == winner(o_wins)

    def test_returns_none_when_game_in_progress(self):
        in_progress = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY]
        ]
        assert winner(in_progress) is None

    def test_returns_none_when_game_a_draw(self):
        draw = [
            [X, O, X],
            [X, O, X],
            [O, X, O]
        ]
        assert winner(draw) is None

class TestTerminal():

    def test_returns_true_given_winner(self):
        winner = [
            [X, X, X],
            [O, O, X],
            [X, O, O]
        ]
        assert terminal(winner)
    
    def test_returns_true_given_draw(self):
        draw = [
            [X, O, X],
            [X, O, X],
            [O, X, O]
        ]
        assert terminal(draw)

    def test_returns_true_given_ongoing_game(self):
        ongoing = [
            [X, EMPTY, O],
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY]
        ]
        assert not terminal(ongoing)

class TestUtility():

    def test_returns_1_when_x_winner(self):
        x_wins = [
            [X, X, X],
            [O, O, X],
            [X, O, O]
        ]
        assert 1 == utility(x_wins)

    def test_returns_minus_1_when_o_winner(self):
        o_wins = [
            [X, O, O],
            [X, X, O],
            [EMPTY, X, O]
        ]
        assert -1 == utility(o_wins)

    def test_returns_0_when_game_a_draw(self):
        draw = [
            [X, O, X],
            [X, O, X],
            [O, X, O]
        ]
        assert 0 == utility(draw)

    
class TestFindMax():

    def test_base_case_(self):
        x_wins = [
            [X, X, X],
            [O, O, X],
            [X, O, O]
        ]
        o_wins = [
            [X, O, O],
            [X, X, O],
            [EMPTY, X, O]
        ]
        draw = [
            [X, O, X],
            [X, O, X],
            [O, X, O]
        ]
        assert find_max(x_wins) == 1
        assert find_max(o_wins) == -1
        assert find_max(draw) == 0

    def test_lvl_one_recursion(self):
        board = [
            [X, X, EMPTY],
            [O, O, X],
            [X, O, O]
        ]
        assert find_max(board) == 1

    def test_lvl_three_recursion(self):
        board = [
            [X, EMPTY, EMPTY],
            [O, EMPTY, X],
            [X, O, O]
        ]
        assert find_max(board) == 1


class TestFindMin():

    def test_base_case_(self):
        x_wins = [
            [X, X, X],
            [O, O, X],
            [X, O, O]
        ]
        o_wins = [
            [X, O, O],
            [X, X, O],
            [EMPTY, X, O]
        ]
        draw = [
            [X, O, X],
            [X, O, X],
            [O, X, O]
        ]
        assert find_min(x_wins) == 1
        assert find_min(o_wins) == -1
        assert find_min(draw) == 0

    def test_lvl_two_recursion(self):
        board = [
            [X, X, EMPTY],
            [O, EMPTY, X],
            [X, O, O]
        ]
        assert find_min(board) == 0


@pytest.mark.skip
class TestMinimax():
    ...