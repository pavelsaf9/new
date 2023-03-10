def check_words(s='python'):
    words = [s, ]
    while word := input('Введите слово: '):
        if word in words:
            print('Строка', word, 'уже присутствует в списке на позиции',
                  words.index(word))
            break
        words.append(word)
    else:
        print('Список слов', words)


check_words()


# def check_words(s='python'):
#     words = [s, ]
#     while word := input("Введите слово: "):
#         if word in words:
#             print('Строка', word, 'уже присутствует в списке на позиции',
#                   words.index(word))
#             break
#         words.append(word)
#     print('Список слов', words)
#
#
# check_words()
