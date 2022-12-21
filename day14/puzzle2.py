class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self):
        return hash(tuple((self.x, self.y)))


# variables
cave_map = {}
max_y = None
count = 1

# const values
ROCK = 1
SAND = 2

sand_entry_point = Point(500, 0)


def check_max_y(y):
    """Determined the largest y (edge of the abyss)

    Args:
        y (int): any y value larger that this is off in the abyss
    """
    global max_y
    if max_y is None or max_y < y:
        max_y = y


def populate_map(formation: str) -> None:
    """Convert a string to a rock formation

    Args:
        formation (str): Set of points describing the formation ex(x1,y1 -> x1,y2 -> x2,y2)
    """
    points = list(map(str.strip, formation.split("->")))

    prev_x = None
    prev_y = None

    for point in points:
        x, y = map(int, point.split(','))
        check_max_y(y)
        if prev_x is not None:
            if x == prev_x:
                for y_val in range(min(y, prev_y), max(y, prev_y) + 1):
                    cave_map[Point(x, y_val)] = ROCK
            else:
                for x_val in range(min(x, prev_x), max(x, prev_x) + 1):
                    cave_map[Point(x_val, y)] = ROCK

            prev_x = x
            prev_y = y
        else:
            prev_x = x
            prev_y = y
            cave_map[Point(x, y)] = ROCK


def check_for_collision(current_sand_point: Point) -> bool:
    """Determine if the sand has hit something

    Args:
        current_sand_point (Point): Current x and y of falling sand

    Returns:
        bool: True if it hit something, False if it is still falling
    """

    for point in list(filter(lambda key: key.x == current_sand_point.x, cave_map.keys())):
        if point.y == current_sand_point.y + 1:
            return True

    if current_sand_point.y + 1 == max_y:
        return True

    return False


def calculate_falling_sand(start_point: Point) -> bool:
    """Calculate the reset position of the falling sand

    Args:
        start_point (Point): Starting point for the fall

    Returns:
        bool: True if the sand come to a stop, False if the sand heads to the abyss
    """
    stopped = False

    # Sand already occupies this spot, we're done
    if check_for_collision(start_point) \
            and Point(start_point.x - 1, start_point.y + 1) in cave_map.keys() \
            and Point(start_point.x + 1, start_point.y + 1) in cave_map.keys():
        cave_map[Point(start_point.x, start_point.y)] = SAND
        return False

    potential_point = Point(start_point.x, start_point.y)

    while stopped == False:
        if check_for_collision(potential_point):
            # is there anything down and to the left?
            if Point(potential_point.x - 1, potential_point.y + 1) not in cave_map.keys() and potential_point.y + 1 < max_y:
                potential_point = Point(
                    potential_point.x - 1, potential_point.y + 1)
                # print(f"Move down and left to {potential_point}")
            # is there anything down and to the right?
            elif Point(potential_point.x + 1, potential_point.y + 1) not in cave_map.keys() and potential_point.y + 1 < max_y:
                potential_point = Point(
                    potential_point.x + 1, potential_point.y + 1)
                # print(f"Move down and right to {potential_point}")
            else:
                print(f"Occupy {potential_point}")
                cave_map[Point(potential_point.x, potential_point.y)] = SAND
                stopped = True
        else:
            potential_point = Point(potential_point.x, potential_point.y + 1)
            # print(f"Move down to {potential_point}")

    return stopped


def get_total_sand() -> int:
    total = 0

    for item in cave_map.values():
        if item == SAND:
            total += 1

    return total


def print_the_map():
    _min_x = None
    _min_y = None
    _max_x = None
    _max_y = None

    for p in cave_map.keys():
        if _min_x is None or _min_x > p.x:
            _min_x = p.x
        if _min_y is None or _min_y > p.y:
            _min_y = p.y
        if _max_x is None or _max_x < p.x:
            _max_x = p.x
        if _max_y is None or _max_y < p.y:
            _max_y = p.y

    print(_min_x, _min_y, _max_x, _max_y)

    rows = []

    for y in range(_min_y - 1, _max_y + 1):
        row = ""
        for x in range(_min_x - 2, _max_x + 3):
            p = Point(x, y)
            if p == sand_entry_point:
                row += 's'
            if p in cave_map.keys():
                val = '#' if cave_map[p] == ROCK else 'o'
                row += val
            else:
                row += '.'

        rows.append(row)

    rows.append("#" * (len(rows[0])+1))
    for r in rows:
        print(r)


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in list(map(str.strip, lines)):
        populate_map(line)

    check_max_y(max_y + 2)

running = True

while running:
    running = calculate_falling_sand(sand_entry_point)
    count += 1

# print(cave_map)
print(f"Total sand: {get_total_sand()}")
# print_the_map()
