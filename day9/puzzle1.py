points = []

head_x = 0
head_y = 0

tail_x = 0
tail_y = 0


def move_tail(dir):
    global head_x
    global head_y
    global tail_x
    global tail_y

    # diagnol move
    if head_x != tail_x and head_y != tail_y and (abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1):
        if dir == "U":
            tail_y += 1
            tail_x = head_x
        elif dir == "D":
            tail_y -= 1
            tail_x = head_x
        elif dir == "R":
            tail_y = head_y
            tail_x += 1
        elif dir == "L":
            tail_y = head_y
            tail_x -= 1
    else:
        if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
            if dir == "U":
                tail_y += 1
            elif dir == "D":
                tail_y -= 1
            elif dir == "R":
                tail_x += 1
            elif dir == "L":
                tail_x -= 1

    output.append(f"({head_x}, {head_y}) - ({tail_x}, {tail_y}) --")
    if (tail_x, tail_y) not in points:
        points.append((tail_x, tail_y))


def move(dir, dist):
    global head_x
    global head_y

    if dir == "U":
        for d in range(1, dist + 1):
            head_y += 1
            move_tail(dir)
    elif dir == "D":
        for d in range(1, dist + 1):
            head_y -= 1
            move_tail(dir)
    elif dir == "R":
        for d in range(1, dist + 1):
            head_x += 1
            move_tail(dir)
    elif dir == "L":
        for d in range(1, dist + 1):
            head_x -= 1
            move_tail(dir)


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        dir, dist = line.strip().split(" ")
        move(dir, int(dist))

print(len(points))
