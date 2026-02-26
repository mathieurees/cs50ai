from tictactoe import EMPTY, X, O, player

class TestPlayer():

    def test_player_returns_X_for_empty_board(self):
        empty_board =   [[EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        assert player(empty_board) == X

    def test_player_returns_X_for_nonempty_board(self):
        empty_board =   [[X, EMPTY, O],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]
        assert player(empty_board) == X

    def test_player_returns_O_for_nonempty_board(self):
        empty_board =   [[X, EMPTY, O],
                         [EMPTY, X, O],
                         [EMPTY, X, EMPTY]]
        assert player(empty_board) == O

