word = input('Введите строку: ')

if len(word) > 100:
    print("Количество символов не должно быть больше 100!")
else:
    if len(word) % 10:
        symbol = "символ"
    elif len(word):
        symbol = "символа"
    else:
        symbol = "символов"
    print("В строке", len(word), symbol)
