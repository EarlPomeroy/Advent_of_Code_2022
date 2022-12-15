class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

class Node:
    def __init__(self, value:Point, dist:int = None) -> None:
        self.value = value # (x, y) tuple
        self.start_dist = dist # g
        self.ending_dist = None # h
        self.weighting = None # f = g + h
        self.parent = None
    
    def __eq__(self, other: object) -> bool:
        return other.value.x == self.value.x and other.value.y == self.value.y

    def __str__(self) -> str:
        return "({}, {})".format(self.value.x, self.value.y)

    def set_heuristics(self, cost):
        self.ending_dist = cost
        self.weighting = self.start_dist + self.ending_dist

class Field:
    def __init__(self, field) -> None:
        self.field = field
        self.open = []
        self.closed = []

    def can_move(self, begin:Point, end:Point):
        if 0 <= end.y and end.y < len(self.field) and 0 <= end.x and end.x < len(self.field[0]):
            start_val = self.field[begin.y][begin.x]
            if start_val == 'S':
                start_val = 'a'

            end_val = self.field[end.y][end.x]
            if end_val == 'E':
                end_val = 'z'

            if (ord(end_val) - ord(start_val)) <= 1:
                return True

        return False

    def find_lowest_cost_point(self):
        lowest = None
        for node in self.open:
            if lowest is None or node.weighting < lowest.weighting:
                lowest = node

        return lowest

    def find_point(self, value):
        for i, row in enumerate(self.field):
            if value in row:
                return Point(row.index(value), i)

    def find_points(self, value):
        points = []
        for i, row in enumerate(self.field):
            for j, col in enumerate(row):
                if self.field[i][j] == value:
                    p = Point(j, i)
                    neighbors = self.get_neighbors(Node(p, 0))

                    for n in neighbors:
                        # an 'a' has to have a b next to it to move on, otherwise it is an island and 
                        # takes forever to process
                        if ord(self.field[n.value.y][n.value.x]) - ord(self.field[p.y][p.x]) == 1:
                            points.append(p)

        return points

    def get_neighbors(self, current):
        neighbors = []

        for i in range(0,4):
            end = None
            match i:
                case 0:
                    end = Point(current.value.x, current.value.y - 1)
                case 1:
                    end = Point(current.value.x, current.value.y + 1)
                case 2:
                    end = Point(current.value.x - 1, current.value.y)
                case 3:
                    end = Point(current.value.x + 1, current.value.y)

            if self.can_move(current.value, end):
                n = Node(end, current.start_dist + 1)
                if n not in self.closed:
                    neighbors.append(n)
        
        return neighbors

    def heuristic_dist_cost(self, current:Node, goal:Node):
        cost = abs(current.value.x - goal.value.x)**2 + abs(current.value.y - goal.value.y)**2
        if current.ending_dist is None or current.ending_dist > cost:
            # current.set_heuristics(cost)
            current.set_heuristics(0)

        return current

    def evaluate(self, start, goal):
        self.heuristic_dist_cost(start, goal)
        self.open.append(start)

        while len(self.open) > 0:
            current = self.find_lowest_cost_point()


            if current is None:
                return None

            if current == goal:
                return current.start_dist

            nodes = self.get_neighbors(current)

            for node in nodes:
                self.heuristic_dist_cost(node, goal)
                node.parent = current
                if node not in self.open:
                    self.open.append(node)

            self.open.remove(current)
            self.closed.append(current)
        
        return None
    def reset(self):
        self.open = []
        self.closed = []

points = []

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in list(map(str.strip, lines)):
        points.append(list(line))


field = Field(points)
s_start_point = field.find_point('S')
a_start_points = field.find_points('a')
end_point = field.find_point('E')

a_start_points.append(s_start_point)

print(f"Length of start points is {len(a_start_points)}")

result = None
goal = Node(end_point)

for s in a_start_points:
    field.reset()
    start = Node(s, 0)

    r = field.evaluate(start, goal)

    if r is not None and (result is None or result > r):
        result = r


if result is None:
    print("No route to goal from any start location")
else:
    print(f"Found route of length {result}")


