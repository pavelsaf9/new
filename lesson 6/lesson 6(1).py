def symbol_words():
    """
Функция считает количество символов во входящей строке без учёта пробелов
    """
    words = input('Введите предложение: ')
    words_1 = len(words) - words.count(' ')
    print('Количество символов в предложении:', words_1)


symbol_words()
print(symbol_words.__doc__)
