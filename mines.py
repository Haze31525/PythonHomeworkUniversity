import random
import sys


def create_board(m, n, p):
    board = [[0 for j in range(n + 2)] for i in range(m + 2)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if random.random() < p:
                board[i][j] = "*"
            else:
                board[i][j] = "."
    return board


def print_board(board, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(board[i][j], end=" ")
        print()


def get_adjacent_mines(board, i, j):
    mines = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if board[x][y] == "*":
                mines += 1
    return mines


def create_minefield(board, m, n):
    minefield = [[0 for j in range(n + 2)] for i in range(m + 2)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if board[i][j] == "*":
                minefield[i][j] = "*"
            else:
                minefield[i][j] = get_adjacent_mines(board, i, j)
    return minefield


def print_minefield(minefield, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(minefield[i][j], end=" ")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python mines.py m n p")
        sys.exit(1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])
    p = float(sys.argv[3])

    board = create_board(m, n, p)
    print("Board:")
    print_board(board, m, n)

    minefield = create_minefield(board, m, n)
    print("Minefield:")
    print_minefield(minefield, m, n)
