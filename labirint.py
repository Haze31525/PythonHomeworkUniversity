import random
import os


def generate_maze(rows, cols, start_row, start_col):
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i == start_row and j == start_col:
                row.append("*")
            elif random.randint(0, 3) == 0:
                row.append("x")
            else:
                row.append("0")
        maze.append(row)
    return maze


def print_maze(maze):
    for row in maze:
        print(" ".join(row))


def get_neighbors(maze, row, col):
    neighbors = []
    if row > 0 and maze[row - 1][col] != "x":
        neighbors.append((row - 1, col))
    if row < len(maze) - 1 and maze[row + 1][col] != "x":
        neighbors.append((row + 1, col))
    if col > 0 and maze[row][col - 1] != "x":
        neighbors.append((row, col - 1))
    if col < len(maze[0]) - 1 and maze[row][col + 1] != "x":
        neighbors.append((row, col + 1))
    return neighbors


def bfs(maze, start_row, start_col):
    visited = set()
    queue = [(start_row, start_col, 0)]
    while queue:
        row, col, steps = queue.pop(0)
        if maze[row][col] == "x":
            continue
        if (row, col) in visited:
            continue
        visited.add((row, col))
        maze[row][col] = str(steps)
        if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1:
            return steps
        for neighbor in get_neighbors(maze, row, col):
            queue.append((neighbor[0], neighbor[1], steps + 1))
    return -1


def main():
    rows = 10
    cols = 20
    start_row = random.randint(1, rows - 2)
    start_col = random.randint(1, cols - 2)
    maze = generate_maze(rows, cols, start_row, start_col)
    print_maze(maze)
    input("Press any key to start...")
    os.system('cls' if os.name == 'nt' else 'clear')
    steps = bfs(maze, start_row, start_col)
    while steps != -1:
        print_maze(maze)
        print("Steps left: ", steps)
        input("Press any key to move...")
        os.system('cls' if os.name == 'nt' else 'clear')
        steps -= 1
    print_maze(maze)
    print("Congratulations, you made it out!")


if __name__ == '__main__':
    main()
