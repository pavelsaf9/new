import random


def guess_number():
    target = random.randint(1, 10)

    for i in range(3):
        guess = input("Введите число от 1 до 10: ")

        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                raise ValueError("Ошибка! Вы ввели не число")

            if guess == target:
                print("Ты победил!")
                return
            elif guess < target:
                print("Ваше число меньше.")
            else:
                print("Ваше число больше.")
        except ValueError:
            print('Ошибка! Введите число от 1 до 10.')

    print("Удача не на твоей стороне, попробуй ещё!")


guess_number()
