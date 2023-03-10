num = int(input('Введите месяц от 1 до 12: '))

months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май',
          6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь',
          11: 'Ноябрь', 12: 'Декабрь'}

if num < 1 or num > 12:
    print("Введите число от 1 до 12")
else:
    if num <= 2 or num == 12:
        print('Зима', months[num], sep=', ')
    elif 3 <= num <= 5:
        print('Весна', months[num], sep=', ')
    elif 6 <= num <= 8:
        print('Лето', months[num], sep=', ')
    else:
        print('Осень', months[num], sep=', ')
