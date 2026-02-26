from tictactoe import initial_state, EMPTY, X, O, player, actions

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
            [EMPTY, O, EMPTY]
        ]
        expected = [
            (0, 1), (1, 0), (1, 1), 
            (1, 2), (2, 0), (2, 2)
        ]
        assert expected == actions(board)