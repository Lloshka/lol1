import random
grid = [[0 for _ in range(10)] for _ in range(10)]
for _ in range(6):
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    grid[row][col] = 'X'
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'X':
            continue
        count = 0
        for ni in range(max(0, i-1), min(10, i+2)):
            for nj in range(max(0, j-1), min(10, j+2)):
                if grid[ni][nj] == 'X':
                    count += 1
        
        if count == 0:
            grid[i][j] = '-'
        else:
            grid[i][j] = str(count)
for row in grid:
    print(' '.join(row))