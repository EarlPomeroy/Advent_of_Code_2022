points = []
knots_x = [0] * 10
knots_y = [0] * 10

def move_tail(knot_index):
    global knots_x
    global knots_y

    if knot_index > 9:
        return

    if abs(knots_x[knot_index - 1] - knots_x[knot_index]) > 1:
        if knots_x[knot_index] > knots_x[knot_index - 1]:
            knots_x[knot_index] -= 1
        else:
            knots_x[knot_index] += 1

        if knots_y[knot_index - 1] != knots_y[knot_index]:
            if knots_y[knot_index] > knots_y[knot_index - 1]:
                knots_y[knot_index] -= 1
            else:
                knots_y[knot_index] += 1
    if abs(knots_y[knot_index - 1] - knots_y[knot_index]) > 1:
        if knots_y[knot_index] > knots_y[knot_index - 1]:
            knots_y[knot_index] -= 1
        else:
            knots_y[knot_index] += 1
        
        if knots_x[knot_index - 1] != knots_x[knot_index]:
            if knots_x[knot_index] > knots_x[knot_index - 1]:
                knots_x[knot_index] -= 1
            else:
                knots_x[knot_index] += 1

    move_tail(knot_index + 1)

    if knot_index == 9 and (knots_x[knot_index], knots_y[knot_index]) not in points:
        points.append((knots_x[knot_index], knots_y[knot_index]))

def move(dir, dist):
    global knots_x
    global knots_y

    if dir == "U":
        for d in range(0, dist):
            knots_y[0] += 1
            move_tail(1)
    elif dir == "D":
        for d in range(0, dist):
            knots_y[0] -= 1
            move_tail(1)
    elif dir == "R":
        for d in range(0, dist):
            knots_x[0] += 1
            move_tail(1)
    elif dir == "L":
        for d in range(0, dist):
            knots_x[0] -= 1
            move_tail(1)


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        dir, dist = line.strip().split(" ")
        move(dir, int(dist))

print(len(points))
