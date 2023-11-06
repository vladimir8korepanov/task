import sys
import math

def read_coordinates(text):
    coordinates = []
    lines = text.split('\n')
    for line in lines:
        if line:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_point_position(center_x, center_y, radius, point_x, point_y):
    distance = calculate_distance(center_x, center_y, point_x, point_y)
    if math.isclose(distance, radius):
        return 0  # точка лежит на окружности
    elif distance < radius:
        return 1  # точка внутри окружности
    else:
        return 2  # точка снаружи окружности

# Проверяем, что переданы два аргумента - имена файлов
if len(sys.argv) != 3:
    print("Необходимо передать два аргумента: файл с координатами и радиусом окружности, и файл с координатами точек.")
    sys.exit(1)

# Считываем содержимое файлов
with open(sys.argv[1], 'r') as file:
    circle_text = file.read()

with open(sys.argv[2], 'r') as file:
    points_text = file.read()

# Считываем координаты и радиус окружности из файла
circle_coordinates = read_coordinates(circle_text)
center_x, center_y, radius = circle_coordinates[0]

# Считываем координаты точек из файла и проверяем их положение относительно окружности
point_coordinates = read_coordinates(points_text)

for point_x, point_y in point_coordinates:
    position = check_point_position(center_x, center_y, radius, point_x, point_y)
    print(position)
