def circular_array(n, m):
    array = list(range(1, n+1))
    path = []
    current_index = 0

    while len(path) < n:
        current_element = array[current_index]
        path.append(current_element)
        next_index = (current_index + m) % n
        current_index = next_index

    return path

# Пример
n = 3
m = 2
result = circular_array(n, m)
print(f'Путь с интервалом длины {m} по заданному круговому массиву: {result}')