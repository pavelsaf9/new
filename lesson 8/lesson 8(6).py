import random


def guess_number():
    target = random.randint(1, 10)

    for i in range(3):
        try:
            guess = int(input("Введите число от 1 до 10: "))
            if guess < 1 or guess > 10:
                print("Введите число от 1 до 10")
            if guess == target:
                print("Ты победил!")
                return
            elif guess < target:
                print("Ваше число меньше.")
            else:
                print("Ваше число больше.")
        except ValueError:
            print("Ошибка вы ввели не число")

    print("Удача не на твоей стороне, попробуй ещё!")


guess_number()
