forest = []

width = 0
height = 0
visible_count = 0


def visible_top(row, col, val):
    for r in range(0, row):
        if forest[r][col] >= val:
            return False

    return True


def visible_bottom(row, col, val):
    for r in range(row + 1, height):
        if forest[r][col] >= val:
            return False

    return True


def visible_left(row, col, val):
    for c in range(0, col):
        if forest[row][c] >= val:
            return False

    return True


def visible_right(row, col, val):
    for c in range(col + 1, width):
        if forest[row][c] >= val:
            return False

    return True


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        row = list(map(int, list(line.strip())))
        forest.append(row)

width = len(forest[0])
height = len(forest)

for row in range(0, height):
    for col in range(0, width):
        if row == 0 or row == height - 1 or col == 0 or col == width - 1:
            visible_count += 1
        else:
            if visible_top(row, col, forest[row][col]):
                visible_count += 1
            elif visible_bottom(row, col, forest[row][col]):
                visible_count += 1
            elif visible_right(row, col, forest[row][col]):
                visible_count += 1
            elif visible_left(row, col, forest[row][col]):
                visible_count += 1

print(visible_count)
