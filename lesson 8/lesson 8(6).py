import random


def guess_number():
    target = random.randint(1, 10)
    print("Я загадал число от 1 до 10. У тебя есть 3 попытки, чтобы угадать его.")

    for i in range(3):
        guess = input("Попробуй угадать число: ")

        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                raise ValueError("Ошибка! Введите число от 1 до 10.")

            if guess == target:
                print("Ты победил!")
                return
            elif guess < target:
                print("Ваше число меньше.")
            else:
                print("Ваше число больше.")
        except ValueError as e:
            print(e)

    print("Удача не на твоей стороне, попробуй ещё!")


guess_number()