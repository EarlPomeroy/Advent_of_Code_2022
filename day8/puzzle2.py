forest = []

width = 0
height = 0
best_view = 0


def get_view(row, col, val):
    top = 0
    bottom = 0
    left = 0
    right = 0

    # get top
    for r in range(row - 1, -1, -1):
        if forest[r][col] < val:
            top += 1
        elif forest[r][col] == val or forest[r][col] > val:
            top += 1
            break
        else:
            break

    # get bottom
    for r in range(row + 1, height):
        if forest[r][col] < val:
            bottom += 1
        elif forest[r][col] == val or forest[r][col] > val:
            bottom += 1
            break
        else:
            break

    # get left
    for c in range(col - 1, -1, -1):
        if forest[row][c] < val:
            left += 1
        elif forest[row][c] == val or forest[row][c] > val:
            left += 1
            break
        else:
            break

    # get right
    for c in range(col + 1, width):
        if forest[row][c] < val:
            right += 1
        elif forest[row][c] == val or forest[row][c] > val:
            right += 1
            break
        else:
            break

    return top * bottom * right * left


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
            # skip edge trees because multiplication by zero results in a zero
            pass
        else:
            best_view = max(get_view(row, col, forest[row][col]), best_view)

print(best_view)
