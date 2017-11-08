star = [[0, 5, '*', 1, 3], ['*', 'a', '*', '*', 9], [9, '*', 1, 4, '*'], [0, 0, 0, 0, '*'], ['*', '*', '*', '*', '*']]
board = [star, star, star, star, star]

print(board, len(board))
for star in board:
    row_count = 0
    column_count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if star[i][j] == '*':
                row_count += 1
                column_count += 1

for star in board:
    row_numbers = []
    column_numbers = []
    for i in range(len(board)):
        for j in range(len(board)):
            if star[i][j] == '*':
                row_numbers.append(i)
                column_numbers.append(j)

for star in board:
    found_coordinates = []
    for i in range(len(board)):
        for j in range(len(board)):
            if star[i][j] == '*':
                found_coordinates.append((i, j))

print(found_coordinates)
