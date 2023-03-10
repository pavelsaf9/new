import random


def sum_number():
    try:
        num = int(input("Введите число от 1 до 10: "))
        if not 1 <= num <= 10:
            print("Введите число от 1 до 10")
            return
        random_num = random.randint(10, 100)
        start_num = min(num, random_num)
        end_num = max(num, random_num)
        result = sum(range(start_num, end_num+1))
        print(result)
    except ValueError:
        print('Введите число от 1 до 10')


sum_number()