

def start(
        input,
        output
):
    """
    Start endpoint of the application
    :type input: str
    :type output: str
    """
    from application.sudoku import BoardInitializer
    board_builder = BoardInitializer()
    board = board_builder.create()
    from application.sudoku import BoardCleaner
    board_cleaner = BoardCleaner(
        board=board,
        empty_char=board_builder.get_empty(),
        space_char=board_builder.get_space(),
        split_char=board_builder.get_split(),
        null_char=board_builder.get_null()
    )
    board_elements = board_cleaner.process_board()
    save_board(
        board=board_elements,
        filename=input
    )
    from application.sudoku import SudokuSolver
    solver = SudokuSolver(
        board=board_elements,
        null_char=board_builder.get_null()
    )
    solver.solve()
    board_solution = solver.get_solution()
    save_board(
        board=board_solution,
        filename=output
    )


def save_board(
        board,
        filename
):
    """
    Save the board into the file
    :type board: list
    :type filename: str
    """
    with open(filename, 'w') as file:
        for board_row in board:
            for board_element in board_row:
                file.write(str(board_element))
                file.write(" ")
            file.write("\n")
