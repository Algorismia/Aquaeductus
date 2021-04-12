import sys
import math


class Point:

    @staticmethod
    def middle_with_y(first_point: 'Point', second_point: 'Point', y_coord: int) -> 'Point':
        return Point((first_point.x_coord + second_point.x_coord) / 2, y_coord)

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def x_distance_to(self, second_point: 'Point') -> int:
        return second_point.x_coord - self.x_coord

    def y_distance_to(self, second_point: 'Point') -> int:
        return second_point.y_coord - self.y_coord

    def distance(self, second_point: 'Point') -> float:
        return math.sqrt(pow(self.x_distance_to(second_point), 2) + \
                         pow(self.y_distance_to(second_point), 2))


class Land:

    def __init__(self, num_points: str, max_height: str, alpha: str, beta: str):
        self.num_points = int(num_points)
        self.max_height = int(max_height)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.points = []
        self.point_values_buffer = [None] * self.num_points

    def add_point_to_land(self, x_coord: int, y_coord: int):
        self.points.append(Point(x_coord, y_coord))

    def cost_arch(self, first_point: Point, second_point: Point):
        return self.beta * pow(first_point.x_distance_to(second_point), 2)

    def cost_support(self, point: Point):
        return self.alpha * (self.max_height - point.y_coord)

    def total_cost(self, first_point_index: int, second_point_index: int):
        cost_second_point = self.point_values_buffer[second_point_index]
        cost_arch = self.cost_arch(self.points[first_point_index], self.points[second_point_index])
        cost_first_point = self.cost_support(self.points[first_point_index])
        if cost_second_point:
            return cost_first_point + cost_arch + cost_second_point
        cost_second_point = self.cost_support(self.points[second_point_index])
        return cost_first_point + cost_arch + cost_second_point

    @staticmethod
    def out_of_circunference(radius_point: Point, radius_value: int, point: Point):
        return (pow(radius_point.distance(point), 2) - (pow(radius_value, 2))) > 0

    def valid_arch(self, first_point_index: int, second_point_index: int):
        first_point = self.points[first_point_index]
        second_point = self.points[second_point_index]
        radius_value = first_point.x_distance_to(second_point) / 2
        init_arch = self.max_height - radius_value
        radius_point = Point.middle_with_y(first_point, second_point, init_arch)
        if init_arch < first_point.y_coord or init_arch < second_point.y_coord:
            return False
        for i in range(first_point_index + 1, second_point_index):
            out_of_circle = Land.out_of_circunference(radius_point, radius_value, self.points[i])
            if self.points[i].y_coord >= init_arch and out_of_circle:
                return False
        return True

    def get_minimum_cost_for_index(self, index: int) -> int:
        minimum = math.inf
        for i in range(index + 1, self.num_points):
            if self.valid_arch(index, i):
                cost_points = self.total_cost(index, i)
                if cost_points < minimum:
                    minimum = cost_points
        return minimum

    def get_minimum_aqueduct(self):
        for i in range(self.num_points - 2, -1, -1):
            minimum_of_this_point = self.get_minimum_cost_for_index(i)
            self.point_values_buffer[i] = minimum_of_this_point
        return self.point_values_buffer[0]


def get_land_from_file(file_name: str) -> Land:
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        num_points, max_height, alpha, beta = lines[0].split(" ")
        land = Land(num_points, max_height, alpha, beta)
        add_points_to_land(land, lines[1:])
        file.close()
        return land
    except (FileNotFoundError, ValueError, IndexError):
        print(f"File {file_name} doesn't exist or has an invalid syntax")
        sys.exit(-1)


def add_points_to_land(land: Land, points: list):
    for point in points:
        x_coord, y_coord = point.split("\n")[0].split(" ")
        land.add_point_to_land(int(x_coord), int(y_coord))


def get_file_name() -> str:
    if len(sys.argv) == 2:
        return sys.argv[1]
    file_name = input("Enter file name: ")
    return file_name


def main():
    file_name = get_file_name()
    land = get_land_from_file(file_name)
    value = land.get_minimum_aqueduct()
    if value == math.inf:
        print("impossible")
    else:
        print(value)


if __name__ == "__main__":
    main()
