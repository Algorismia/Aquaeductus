import sys
import math


class Point:

    @staticmethod
    def middle_with_y(first_point: 'Point', second_point: 'Point', y: int) -> 'Point':
        return Point((first_point.x + second_point.x) / 2, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x_distance_to(self, second_point: 'Point') -> int:
        return second_point.x - self.x

    def y_distance_to(self, second_point: 'Point') -> int:
        return second_point.y - self.y

    def distance(self, second_point: 'Point') -> float:
        return math.sqrt(pow(self.x_distance_to(second_point), 2) + pow(self.y_distance_to(second_point), 2))


class Land:

    def __init__(self, NUM_POINTS: str, MAX_HEIGHT: str, ALPHA: str, BETA: str):
        self.NUM_POINTS = int(NUM_POINTS)
        self.MAX_HEIGHT = int(MAX_HEIGHT)
        self.ALPHA = int(ALPHA)
        self.BETA = int(BETA)
        self.points = []
        self.point_values_buffer = [None] * self.NUM_POINTS

    def add_point_to_land(self, x: int, y: int):
        self.points.append(Point(x, y))

    def cost_arch(self, first_point: Point, second_point: Point):
        return self.BETA * pow(first_point.x_distance_to(second_point), 2)

    def cost_support(self, point: Point):
        return self.ALPHA * (self.MAX_HEIGHT - point.y)

    def total_cost(self, first_point_index: int, second_point_index: int):
        cost_second_point = self.point_values_buffer[second_point_index]
        if cost_second_point:
            return self.cost_support(self.points[first_point_index]) + self.cost_arch(self.points[first_point_index], self.points[second_point_index]) + cost_second_point
        else:
            return self.cost_support(self.points[first_point_index]) + self.cost_support(self.points[second_point_index]) + self.cost_arch(self.points[first_point_index], self.points[second_point_index])

    def valid_arch(self, first_point_index: int, second_point_index: int):
        first_point = self.points[first_point_index]
        second_point = self.points[second_point_index]
        radius_value = first_point.x_distance_to(second_point) / 2
        init_arch = self.MAX_HEIGHT - radius_value
        radius_point = Point.middle_with_y(first_point, second_point, init_arch)
        if init_arch < first_point.y or init_arch < second_point.y:
            return False
        for i in range(first_point_index + 1, second_point_index):
            if self.points[i].y >= init_arch and (
                    pow(radius_point.distance(self.points[i]), 2) - (radius_value * radius_value)) > 0:
                return False
        return True

    def get_minimum_cost_for_index(self, index: int) -> int:
        minimum = math.inf
        for i in range(index + 1, self.NUM_POINTS):
            if self.valid_arch(index, i):
                cost_points = self.total_cost(index, i)
                if cost_points < minimum:
                    minimum = cost_points
        return minimum

    def get_minimum_aqueduct(self):
        for i in range(self.NUM_POINTS - 2, -1, -1):
            minimum_of_this_point = self.get_minimum_cost_for_index(i)
            self.point_values_buffer[i] = minimum_of_this_point
        return self.point_values_buffer[0]


def get_land_from_file(file_name: str) -> Land:
    file = open(file_name, "r")
    lines = file.readlines()
    first_line = lines[0].split(" ")
    land = Land(first_line[0], first_line[1], first_line[2], first_line[3])
    add_points_to_land(land, lines[1:])
    file.close()
    return land


def add_points_to_land(land: Land, points: list):
    for point in points:
        x, y = point.split("\n")[0].split(" ")
        land.add_point_to_land(int(x), int(y))


if __name__ == "__main__":
    land = get_land_from_file(sys.argv[1])
    value = land.get_minimum_aqueduct()
    if value == math.inf:
        print("impossible")
    else:
        print(value)
