def parseBoard(inputBoard) -> list(list[int]):
    board: list(list[int]) = [[0]]
    if isinstance(inputBoard, str):
        # if the string is only 81 numbers
        # interpret it as 9 x 9, split as rows
        if len(inputBoard) == 81:
            board = [
                [int(char) for char in inputBoard[row * 9 : (row + 1) * 9]]
                for row in range(len(inputBoard) // 9)
            ]

    return board


def board2str(inputBoard: list(list[int])) -> str:
    flatBoard = sum(inputBoard, [])
    boardStr = ""
    for num in flatBoard:
        boardStr += str(num)
    return boardStr


def constructBoard(board: list(list[int])) -> list(list[int]):
    if board == [[1]]:
        board.pop()
        # Example solved board
        board.append([1, 9, 8, 7, 6, 5, 4, 3, 2])
        board.append([2, 1, 9, 8, 7, 6, 5, 4, 3])
        board.append([3, 2, 1, 9, 8, 7, 6, 5, 4])
        board.append([4, 3, 2, 1, 9, 8, 7, 6, 5])
        board.append([5, 4, 3, 2, 1, 9, 8, 7, 6])
        board.append([6, 5, 4, 3, 2, 1, 9, 8, 7])
        board.append([7, 6, 5, 4, 3, 2, 1, 9, 8])
        board.append([8, 7, 6, 5, 4, 3, 2, 1, 9])
        board.append([9, 8, 7, 6, 5, 4, 3, 2, 1])
    return board


def transposeBoard(board: list(list[int])) -> list(list[int]):
    boardT: list(list[int]) = [[] for n in range(9)]
    for rowNum in range(len(board[0])):
        for colNum in range(len(board)):
            boardT[rowNum].append(board[colNum][rowNum])
    return boardT


def checkBoard(board: list(list[int])) -> bool:
    facit: set[int] = set(range(1, 10))
    for row in board:
        if not set(row) == facit:
            return False

    boardT = transposeBoard(board)
    for col in boardT:
        if not set(col) == facit:
            return False

    subBoards = []
    for rowNum in range(len(board) // 3):
        for colNum in range(len(board[0]) // 3):
            subBoards.append(
                sum(
                    [
                        sub[3 * colNum : 3 * (colNum + 1)]
                        for sub in board[3 * rowNum : 3 * (rowNum + 1)]
                    ],
                    [],
                )
            )
    for subBoard in subBoards:
        if not set(subBoard) == facit:
            return False
    return True


def printBoard(board: list(list[int])) -> None:
    for arr in board:
        print(arr)


def testingPrint(boardStr: str) -> None:
    testingBoard = parseBoard(boardStr)
    print(f"The provided sudoku is solved? {checkBoard(testingBoard)}")
    printBoard(testingBoard)


def test() -> None:
    testingPrint(
        "046010520500480000139500080090100270000003045704800001000000067400035900012790400"
    )
    testingPrint(
        "846317529527489136139526784395164278281973645764852391953241867478635912612798453"
    )
    testingPrint(
        "198765432219876543321987654432198765543219876654321987765432198876543219987654321"
    )
