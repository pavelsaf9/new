def check_words(s='python'):
    words = [s, ]
    while True:
        word = input("Введите слово: ")
        if not word:
            print("Список слов:", words)
            break
        if word in words:
            print('Строка', word, 'уже присутствует в списке на позиции',
                  words.index(word))
            break
        else:
            words.append(word)


check_words()

