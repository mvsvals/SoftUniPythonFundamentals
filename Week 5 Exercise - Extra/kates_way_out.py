input_rows = int(input())
maze = [list(input().rstrip()) for _ in range(input_rows)]
kate_initial_x, kate_initial_y = 0, 0

for i in range(input_rows):
    for j in range(len(maze[i])):
        if maze[i][j] == 'k':
            kate_initial_x = i
            kate_initial_y = j

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * len(maze[0]) for _ in range(input_rows)]
max_moves = 0

def dfs(x, y, moves):
    global max_moves
    visited[x][y] = True
    if (x == 0 or x == input_rows - 1 or y == 0 or y == len(maze[0]) - 1) and maze[x][y] == ' ':
        max_moves = max(max_moves, moves + 1)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < input_rows and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == ' ' and not visited[nx][ny]:
                dfs(nx, ny, moves + 1)
    visited[x][y] = False

dfs(kate_initial_x, kate_initial_y, 0)

if max_moves > 0:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
