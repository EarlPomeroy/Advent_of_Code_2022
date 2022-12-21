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

    return False


def calculate_falling_sand(start_point: Point) -> bool:
    """Calculate the reset position of the falling sand

    Args:
        start_point (Point): Starting point for the fall

    Returns:
        bool: True if the sand come to a stop, False if the sand heads to the abyss
    """
    stopped = False

    contact_point = Point(start_point.x, start_point.y + 1)

    while contact_point.y < max_y and stopped == False:
        if check_for_collision(contact_point):
            # is there anything down and to the left?
            if Point(contact_point.x - 1, contact_point.y + 1) not in cave_map.keys():
                contact_point = Point(contact_point.x - 1, contact_point.y + 1)
            # is there anything down and to the right?
            elif Point(contact_point.x + 1, contact_point.y + 1) not in cave_map.keys():
                contact_point = Point(contact_point.x + 1, contact_point.y + 1)
            else:
                cave_map[Point(contact_point.x, contact_point.y)] = SAND
                stopped = True
        else:
            contact_point = Point(contact_point.x, contact_point.y + 1)

    return stopped


def get_total_sand() -> int:
    total = 0

    for item in cave_map.values():
        if item == SAND:
            total += 1

    return total


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in list(map(str.strip, lines)):
        populate_map(line)


running = True

while running:
    running = calculate_falling_sand(sand_entry_point)

print(cave_map)
print(f"Total sand: {get_total_sand()}")
