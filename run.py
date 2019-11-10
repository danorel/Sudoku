

def argument_namespace():
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description="Sudoku solver"
    )
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        help="Input Sudoku board"
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help="Output Sudoku board"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = argument_namespace()
    from application import start
    start(
        input=args.input,
        output=args.output
    )
