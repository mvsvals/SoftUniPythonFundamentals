input_rows = int(input())
maze = [list(input()) for _ in range(input_rows)]
kate_initial_x = -1
kate_initial_y = -1

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

    # Check if Kate is at the edge of the maze
    if (x == 0 or x == input_rows - 1 or y == 0 or y == len(maze[0]) - 1) and maze[x][y] == ' ':
        max_moves = max(max_moves, moves)

    # Explore all four directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < input_rows and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == ' ' and not visited[nx][ny]:  # Only move to empty spaces
                dfs(nx, ny, moves + 1)

    visited[x][y] = False  # Backtrack

dfs(kate_initial_x, kate_initial_y, 0)

# Output the result
if max_moves > 0:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
