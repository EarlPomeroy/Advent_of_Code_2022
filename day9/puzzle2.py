points = []
knots_x = [0] * 10
knots_y = [0] * 10


def move_tail(dir, knot_index):
    global knots_x
    global knots_y

    if knot_index > 9:
        return

    # diagnol move
    if knots_x[knot_index - 1] != knots_x[knot_index] and knots_y[knot_index - 1] != knots_y[knot_index] and (abs(knots_x[knot_index - 1] - knots_x[knot_index]) > 1 or abs(knots_y[knot_index - 1] - knots_y[knot_index]) > 1):
        if dir == "U":
            knots_y[knot_index] += 1
            knots_x[knot_index] = knots_x[knot_index - 1]
        elif dir == "D":
            knots_y[knot_index] -= 1
            knots_x[knot_index] = knots_x[knot_index - 1]
        elif dir == "R":
            knots_y[knot_index] = knots_y[knot_index]
            knots_x[knot_index] += 1
        elif dir == "L":
            knots_y[knot_index] = knots_y[knot_index]
            knots_x[knot_index] -= 1
    else:
        if abs(knots_x[knot_index - 1] - knots_x[knot_index]) > 1 or abs(knots_y[knot_index] - knots_y[knot_index]) > 1:
            if dir == "U":
                knots_y[knot_index] += 1
            elif dir == "D":
                knots_y[knot_index] -= 1
            elif dir == "R":
                knots_x[knot_index] += 1
            elif dir == "L":
                knots_x[knot_index] -= 1

    if knot_index == 9 and (knots_x[knot_index], knots_y[knot_index]) not in points:
        points.append((knots_x[knot_index], knots_y[knot_index]))
    else:
        move_tail(dir, knot_index + 1)


def move(dir, dist):
    global knots_x
    global knots_y

    if dir == "U":
        for d in range(1, dist + 1):
            knots_y[0] += 1
            move_tail(dir, 1)
    elif dir == "D":
        for d in range(1, dist + 1):
            knots_y[0] -= 1
            move_tail(dir, 1)
    elif dir == "R":
        for d in range(1, dist + 1):
            knots_x[0] += 1
            move_tail(dir, 1)
    elif dir == "L":
        for d in range(1, dist + 1):
            knots_x[0] -= 1
            move_tail(dir, 1)


with open("./test.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        dir, dist = line.strip().split(" ")
        move(dir, int(dist))

print(len(points))
