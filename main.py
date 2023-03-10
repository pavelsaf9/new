input_str = 'Pentest'
# Преобразуем строку в список символов
char_list = len(input_str)

# Создаем верхнюю границу
top_border = "+-" * char_list + "+\n"

# Создаем строку со символами, разделенными вертикальной чертой
mid_str = "|" + "|".join(input_str) + "|\n"

# Создаем нижнюю границу
bottom_border = "+-" * char_list + "+"

# Объединяем все три строки
output_str = top_border + mid_str + bottom_border

print(output_str)