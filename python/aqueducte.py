import sys
import math

ALPHA = 0
BETA = 0
MAX_HEIGHT = 0
NUM_POINTS = 0

points_values = {}


# points

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def x_distance(first_point: Point, second_point: Point) -> int:
    return second_point.x - first_point.x


def y_distance(first_point: Point, second_point: Point) -> int:
    return second_point.y - first_point.y


def distance(first_point: Point, second_point: Point) -> float:
    return math.sqrt(pow(x_distance(first_point, second_point), 2) + pow(y_distance(first_point, second_point), 2))


def middle_x(first_point: Point, second_point: Point, y) -> Point:
    return Point((first_point.x + second_point.x) / 2, y)


# cost

def cost_arch(first_point: Point, second_point: Point):
    return BETA * pow(x_distance(first_point, second_point), 2)


def cost_support(point: Point):
    return ALPHA * (MAX_HEIGHT - point.y)


def total_cost(first_point: Point, second_point: Point):
    global points_values
    name_point = f'{second_point.x}, {second_point.y}'
    other = points_values.get(name_point, 0)
    if other == 0:
        return cost_support(first_point) + cost_support(second_point) + cost_arch(first_point, second_point) + other
    else:
        return cost_support(first_point) + cost_arch(first_point, second_point) + other


# arch valid

def valid_arch(points: list, first_point_index: int, second_point_index: int):
    first_point = points[first_point_index]
    second_point = points[second_point_index]
    radius_value = x_distance(first_point, second_point) / 2
    init_arch = MAX_HEIGHT - radius_value
    radius_point = middle_x(first_point, second_point, init_arch)
    if init_arch < first_point.y or init_arch < second_point.y:
        return False
    for i in range(first_point_index + 1, second_point_index):
        if points[i].y >= init_arch and (pow(distance(radius_point, points[i]), 2) - (radius_value * radius_value)) > 0:
            return False
    return True


def get_minimum(points: list, index: int):
    minimum = math.inf
    for i in range(index + 1, len(points)):
        if valid_arch(points, index, i):
            cost_points = total_cost(points[index], points[i])
            if cost_points < minimum:
                minimum = cost_points
    return minimum


def get_minimum_aqueduct(points: list):
    global points_values
    for i in range(len(points) - 2, -1, -1):
        minimum_of_this_point = get_minimum(points, i)
        name_of_current_point = f'{points[i].x}, {points[i].y}'
        points_values[name_of_current_point] = minimum_of_this_point
    name = f"{points[0].x}, {points[0].y}"
    return points_values[name]


def get_value_of_globals_from_file(lines: list):
    global ALPHA, BETA, MAX_HEIGHT, NUM_POINTS
    first = lines[0].split(" ")
    NUM_POINTS = int(first[0])
    MAX_HEIGHT = int(first[1])
    ALPHA = int(first[2])
    BETA = int(first[3])


def get_point_list_from_file(file_lines: list) -> list:
    points = []
    for i in range(1, NUM_POINTS + 1):
        tuple = file_lines[i].split("\n")[0]
        x, y = tuple.split(" ")
        points.append(Point(int(x), int(y)))
    return points


if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    file.close()
    get_value_of_globals_from_file(lines)
    list_points = get_point_list_from_file(lines)
    value = get_minimum_aqueduct(list_points)
    if value == math.inf:
        print("impossible")
    else:
        print(value)
