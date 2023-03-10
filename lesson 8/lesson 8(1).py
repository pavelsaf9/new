def get_number():
    while True:
        try:
            if (num := int(input('Введите число от 10 до 20: '))) \
                    >= 10 and num <= 20:
                print('Вы ввели число:', num)
            else:
                print('Ошибка! Вы ввели не число или число не в диапазоне!')
        except ValueError:
            print('Ошибка! Вы ввели не число или число не в диапазоне!')


get_number()
