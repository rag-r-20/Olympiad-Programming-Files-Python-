rows, cols = map(int, input().split())
initialGrid = [(list(map(str, input().split()))) for _ in range(rows)]

directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
#             right,  left,     up,    down,  right-up, left-up, right-down, left-down   
finalGrid = [['0' for _ in range(cols)] for _ in range(rows)]

for i in range(len(initialGrid)):  # biggest i = number of rows
    for j in range(len(initialGrid[i])):  # biggest j = number of columns
        if initialGrid[i][j] == 'x':
            finalGrid[i][j] = 'x'
        else:
            mineCount = 0
            for x in range(len(directions)):
                new_coord_x = j + directions[x][0]
                new_coord_y = i + directions[x][1]
                if 0 <= new_coord_x < cols and 0 <= new_coord_y < rows:
                    if initialGrid[new_coord_y][new_coord_x] == "x":
                        mineCount += 1
            finalGrid[i][j] = mineCount
    print(" ".join(map(str, finalGrid[i])))

