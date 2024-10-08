#!/usr/bin/python3
""" defines a nqueens"""

import sys


def init_board(n):
    """Initializes an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in board]
    return (board)


def board_deep_copy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deep_copy, board))
    return (board)


def gets_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solu = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solu.append([r, c])
                break
    return (solu)


def x_out(board, row, colm):
    """X out spots on a chessboard.
    All spots where non-attacking queens that can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): Row where a queen was last played.
        colm (int): Column where a queen was last played.
    """
    # X out all forward spots
    for j in range(colm + 1, len(board)):
        board[row][j] = "x"
    # X out all backwards spots
    for j in range(colm - 1, -1, -1):
        board[row][j] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][colm] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][colm] = "x"
    # X out all spots diagonally down to the right
    j = colm + 1
    for r in range(row + 1, len(board)):
        if j >= len(board):
            break
        board[r][j] = "x"
        j += 1
    # X out all spots diagonally up to the left
    j = colm - 1
    for r in range(row - 1, -1, -1):
        if j < 0:
            break
        board[r][j]
        j -= 1
    # X out all spots diagonally up to the right
    j = colm + 1
    for r in range(row - 1, -1, -1):
        if j >= len(board):
            break
        board[r][j] = "x"
        j += 1
    # X out all spots diagonally down to the left
    j = colm - 1
    for r in range(row + 1, len(board)):
        if j < 0:
            break
        board[r][j] = "x"
        j -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(gets_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_deep_copy(board)
            temp_board[row][c] = "Q"
            x_out(temp_board, row, c)
            solutions = recursive_solve(temp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
