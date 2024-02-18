### Solve sudoku using my own algorithm
### Algorithm:
### Compare each row and column against a set of 1-9.
### Should solve it
import sys
from curses import wrapper
from SudokuHelper import *
from SudokuSolver import *
from SudokuTUI import *


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage:\n\t-t\t--test\n\t\tUsed to test")
        print("\t-s\t--solve\n\t\tUsed to solve")
    if "--test" in args or "-t" in args:
        test()
    if ("--solve" in args or "-s" in args) and args[-1] != "--solve":
        solve(args.index("--solve"))

    else:
        print(sys.argv)
        wrapper(tui)


if __name__ == "__main__":

    main()
