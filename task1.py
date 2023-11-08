def find_circle_path(n, m):
    current_index = 0
    circle_array = list(range(1, n + 1))
    path = []

    for _ in range(n):
        next_index = (current_index + m - 1) % n
        path.append(circle_array[next_index])
        del circle_array[next_index]
        n -= 1
        current_index = next_index

    return path

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
path = find_circle_path(n, m)
print(path)
