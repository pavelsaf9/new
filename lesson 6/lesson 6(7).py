def get_offer():
    return input('Введите предложение: ')


def count_chars(offer):
    return len(offer)


def count_word(offer):
    return len(offer.split())


def every_chars(offer):
    for char in sorted(set(offer)):
        print(char, '-', offer.count(char))


def main():
    offer = get_offer()
    print('Символов в предложении:', count_chars(offer))
    print('Слова в предложении:', count_word(offer))
    print('Сколько раз встречается каждый знак: ')
    every_chars(offer)


if __name__ == '__main__':
    main()
