import sys

# Чтение содержимого файла и преобразование в массив целых чисел
with open(sys.argv[1], 'r') as file:
    nums = [int(num) for num in file.read().split()]

# Поиск максимального и минимального значения
max_num = max(nums)
min_num = min(nums)

# Инициализация переменной count
count = 0

# Приведение всех элементов к одному числу
while max_num != min_num:
    if max_num > min_num:
        nums = [num - 1 for num in nums]
    else:
        nums = [num + 1 for num in nums]
    count += 1
    max_num = max(nums)
    min_num = min(nums)

print(count)