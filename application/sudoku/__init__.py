class BoardInitializer:
    def __init__(self):
        self._board = None
        self._empty = "*"
        self._split = "\n"
        self._space = " "
        self._null = "0"

    def create(self) -> str:
        self._board = \
            """
            * * * * * * * 9 7
            * * 7 * * 1 * * *
            6 * * 7 5 * * 3 *
            * * 5 * * 7 * 1 *
            * 3 * * * * 2 * *
            9 1 * 5 * 8 * * 6
            2 * * * * * 7 * *
            * 7 * * * * * 4 9
            3 * * 1 7 * * * *
        """
        return self._board

    def get_empty(self):
        return self._empty

    def get_split(self):
        return self._split

    def get_space(self):
        return self._space

    def get_null(self):
        return self._null


class BoardCleaner:
    def __init__(self,
                 board,
                 empty_char,
                 split_char,
                 space_char,
                 null_char):
        """
        Parse board into the two-dimensional array
        :type board: str
        :type empty_char: str
        :type split_char: str
        :type space_char: str
        :type null_char: str
        """
        self._board = board
        self._empty_char = empty_char
        self._split_char = split_char
        self._space_char = space_char
        self._null_char = null_char

    def process_board(self) -> list:
        board_elements = []
        board_partitions = self._board.split(self._split_char)
        for element in board_partitions:
            board_row = []
            for character in element.split(self._space_char):
                if character == self._empty_char:
                    board_row.append(int(self._null_char))
                elif character.isdecimal():
                    board_row.append(int(character))
            if board_row:
                board_elements.append(board_row)
        return board_elements


class SudokuSolver:
    def __init__(self,
                 board,
                 null_char):
        """
        Initialization step
        :type board: list
        """
        self._board = board
        self._null_char = null_char
        self._is_solved = False
        self._SIZE = 9

    def solve(self) -> bool:
        self._is_solved = self._workout()
        return self._is_solved

    def get_solution(self) -> list:
        if self._is_solved:
            return self._board
        else:
            print("There is no solution! Cannot receive the solved board!")

    def _workout(self) -> bool:
        for row in range(0, self._SIZE):
            for col in range(0, self._SIZE):
                if self._board[row][col] == int(self._null_char):
                    for element in range(1, self._SIZE + 1):
                        if self._is_input_valid(row, col, element):
                            self._board[row][col] = element
                            if self._workout():
                                return True
                            else:
                                self._board[row][col] = int(self._null_char)
                    return False
        return True

    def _in_row(self,
                index,
                element) -> bool:
        return element in self._board[index]

    def _in_col(self,
                index,
                element) -> bool:
        inCol = False
        for row in self._board:
            if row[index] == element:
                inCol = True
        return inCol

    def _in3x3(self,
               row,
               col,
               element) -> bool:
        square_row = row - row % 3
        square_col = col - col % 3
        for row_iter in range(square_row, square_row + 3):
            for col_iter in range(square_col, square_col + 3):
                if element == self._board[row_iter][col_iter]:
                    return True
        return False

    def _is_input_valid(self,
                        row,
                        col,
                        element):
        return (not self._in_row(row, element)) and (not self._in_col(col, element)) and (not self._in3x3(row, col, element))
