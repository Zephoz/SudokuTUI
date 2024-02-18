import curses
from SudokuHelper import *


def board2TUI(board: list(list[int])) -> (str, list[int]):
    testBoard = parseBoard(board)
    retStr = "-" * 25 + "\n"
    count = 0
    for row in testBoard:
        newStr = "| "
        count += 1
        for charInd, char in enumerate(row):
            newStr += str(char) + " "
            if charInd in [2, 5, 8]:
                newStr += "| "
        newStr += "\n"
        retStr += newStr
        if count in [3, 6, 9]:
            retStr += "-" * 25 + "\n"
    return retStr, (len(testBoard[0]), len(testBoard))


def TUI2str(tuiBoard: list[str]) -> str:
    tuiStr = "".join(tuiBoard)
    tuiStr = tuiStr.translate({ord(i): None for i in " \n[]-|"})
    return tuiStr


def tui(stdscr) -> None:
    # Setting up curses
    curses.curs_set(0)

    key = ""
    index = [0, 0]
    board, boardSize = board2TUI(
        "846317529527489136139526784395164278281973645764852391953241867478635912612798453"
    )
    while key != "q":
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            index[0] -= 1
        if key == "KEY_RIGHT":
            index[0] += 1
        if key == "KEY_UP":
            index[1] -= 1
        if key == "KEY_DOWN":
            index[1] += 1
        if key in [str(n) for n in range(1, 10)]:
            board = (
                board[index[1]][: index[0] * 2 + 1]
                + key
                + board[index[1]][index[0] * 2 + 2 :]
            )

        index[0] %= boardSize[0]
        index[1] %= boardSize[1]
        stdscr.clear()

        boardStr = TUI2str(board)
        testPointer = board.find(
            boardStr[index[1] * 9 + index[0]],
            (index[1] + round(index[1] // 3) + 1) * 27 - 1,
        )
        test = board[int(testPointer)]
        board = board[: testPointer - 1] + "[" + test + "]" + board[testPointer + 2 :]
        stdscr.addstr("".join(board))
        stdscr.addstr(f"Index:({index[0]},{index[1]}), boardSize: {boardSize}")
        stdscr.addstr(boardStr)
        stdscr.addstr(f"wtf={test}, placement={testPointer};")
        board, boardSize = board2TUI(boardStr)

        if key == "c":
            stdscr.addstr(
                f"The current board is solved? {checkBoard(parseBoard(boardStr))}"
            )
        stdscr.refresh()
