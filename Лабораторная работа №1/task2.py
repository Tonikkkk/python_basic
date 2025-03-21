# TODO Найдите количество книг, которое можно разместить на дискете
# Данные
disk_capacity_mb = 1.44  # Объем дискеты в Мб
pages_in_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
characters_per_line = 25  # Количество символов в строке
bytes_per_character = 4  # Байты на один символ

# Конвертируем объем дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

# Рассчитаем объем данных одной книги
total_characters = pages_in_book * lines_per_page * characters_per_line
total_bytes_per_book = total_characters * bytes_per_character

# Рассчитаем, сколько книг можно поместить на дискету
books_on_disk = disk_capacity_bytes // total_bytes_per_book

print("Количество книг, помещающихся на дискету:", int(books_on_disk))