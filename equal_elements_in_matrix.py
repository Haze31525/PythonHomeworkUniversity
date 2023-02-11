matrix = [[1, 3, 2, 2, 2, 4],
          [3, 3, 3, 2, 4, 4],
          [4, 3, 1, 2, 3, 2],
          [4, 3, 1, 3, 3, 1],
          [4, 3, 3, 3, 1, 1]]
m, n = len(matrix), len(matrix[0])
x_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
y_dir = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y, matrix, m, n, number, visited):
    count = 1
    visited[x][y] = True
    for i in range(8):
        new_x, new_y = x + x_dir[i], y + y_dir[i]
        if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] == number:
            count += dfs(new_x, new_y, matrix, m, n, number, visited)
    return count

result = 0
visited = [[False for _ in range(n)] for __ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            result = max(result, dfs(i, j, matrix, m, n, matrix[i][j], visited))
print(result)
