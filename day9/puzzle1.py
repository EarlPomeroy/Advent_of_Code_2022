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

    # diagonal move
    if abs(head_x - tail_x) > 1:
        if tail_x > head_x:
            tail_x -= 1
        else:
            tail_x += 1

        if head_y != tail_y:
            if tail_y > head_y:
                tail_y -= 1
            else:
                tail_y += 1
    if abs(head_y - tail_y) > 1:
        if tail_y > head_y:
            tail_y -= 1
        else:
            tail_y += 1
        
        if head_x != tail_x:
            if tail_x > head_x:
                tail_x -= 1
            else:
                tail_x += 1

    if (tail_x, tail_y) not in points:
        points.append((tail_x, tail_y))

def move(dir, dist):
    global head_x
    global head_y

    if dir == "U":
        for d in range(0, dist):
            head_y += 1
            move_tail(dir)
    elif dir == "D":
        for d in range(0, dist):
            head_y -= 1
            move_tail(dir)
    elif dir == "R":
        for d in range(0, dist):
            head_x += 1
            move_tail(dir)
    elif dir == "L":
        for d in range(0, dist):
            head_x -= 1
            move_tail(dir)

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        dir, dist = line.strip().split(" ")
        move(dir, int(dist))

print(len(points))
