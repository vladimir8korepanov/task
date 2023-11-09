import sys


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y, r = map(float, file.readline().split())
    return x, y, r


def read_points(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(circle_x, circle_y, radius, point_x, point_y):
    distance_square = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    if distance_square < radius ** 2:
        return 1  # точка внутри окружности
    elif distance_square > radius ** 2:
        return 2  # точка снаружи окружности
    else:
        return 0  # точка на окружности


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file_path> <points_file_path>")
    else:
        circle_file_path = sys.argv[1]
        points_file_path = sys.argv[2]

        circle_x, circle_y, radius = read_circle_data(circle_file_path)
        points = read_points(points_file_path)

        for point in points:
            result = point_position(circle_x, circle_y, radius, point[0], point[1])
            print(result)
