def area_calculation(*args):
    number = [int(num) for num in args[0]]
    if len(number) == 1:
        pi = 3.14
        radius = number[0] / 2
        area = pi * (radius**2)
        print('Площадь круга:', area, 'кв.м')
    elif len(number) == 2:
        area = number[0]*number[1]
        print('Площадь прямоугольника:', area, 'кв.м')
    elif len(number) == 3:
        a = number[0]
        b = number[1]
        c = number[2]
        perimeter = a + b + c
        p = perimeter / 2
        area = (p*(p - b)*(p - c)) ** 0.5
        print('Площадь треугольника:', area, 'кв.м')
    else:
        print('Необходимо ввести до 3-х аргументов')


area_calculation(input("Введите аргументы: ").split())
