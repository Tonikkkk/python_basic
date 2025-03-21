numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Индекс пропущенного элемента (None)
missing_index = numbers.index(None)
# Список без None для суммы
filtered_numbers = [num for num in numbers if num is not None]
# Вычисляем сумму и количество элементов без пропуска
sum_of_numbers = sum(filtered_numbers)
# Общее количество элементов, включая None
count_of_numbers = len(numbers)
# Вычисляем среднее арифметическое
average = sum_of_numbers / count_of_numbers
# Заменяем None на среднее арифметическое
numbers[missing_index] = average
print("Измененный список:", numbers)