# -*- coding: utf-8 -*-
def area_calculation(*args):
    print(len(args[0]))
    print(type(args))
    print(args[0])
    result = [int(x) for x in args[0]]
    print(result[0], result[1])


area_calculation(input("Введите аргументы: ").split())
