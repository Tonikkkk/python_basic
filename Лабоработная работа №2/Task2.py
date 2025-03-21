# TODO Напишите функцию find_common_participants
def find_common_participants(str1:str, str2:str, delimiter=','):
    """
    Возвращает список общих имен из двух строк, отсортированный в алфавитном порядке.

    :param str1: Первая строка с именами(фамилиями).
    :param str2: Вторая строка с именами(фамилиями).
    :param delimiter: Разделитель, используемый для разделения имен(фамилий) в строках (по умолчанию ',').
    :return: Список общих имен, отсортированный в алфавитном порядке.
    """
    # Преобразуем строки в множества имен, удаляя лишние пробелы
    set1 = set(name.strip() for name in str1.split(delimiter))
    set2 = set(name.strip() for name in str2.split(delimiter))

    # Находим пересечение множеств
    common = set1 & set2

    # Возвращаем отсортированный список общих имен
    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
if __name__ == '__main__':
    result = find_common_participants(participants_first_group, participants_second_group, '|')
    print(result)