import json

def update_values(tests, values):
    # Создаем словарь из results.json для удобного доступа по id
    results_dict = {result['id']: result['value'] for result in values['results']}

    # Обновляем значения в структуре tests.json
    for test in tests['tests']:
        # Проверяем, есть ли результат для данного теста
        if test['id'] in results_dict:
            test['value'] = results_dict[test['id']]
        # Проверяем, есть ли вложенные значения
        if 'values' in test:
            update_values(test, values)

    return tests

def create_report(tests_file, values_file, report_file):
    # Загружаем данные из файлов
    with open(tests_file, 'r') as tests_file:
        tests = json.load(tests_file)
    with open(values_file, 'r') as values_file:
        values = json.load(values_file)

    # Обновляем значения в структуре tests.json
    updated_tests = update_values(tests, values)

    # Сохраняем обновленную структуру в файл report.json
    with open(report_file, 'w') as report_file:
        json.dump(updated_tests, report_file)

# Пример использования
tests_file = 'tests.json'
values_file = 'values.json'
report_file = 'report.json'
create_report(tests_file, values_file, report_file)
print(f"Файл {report_file} успешно создан.")