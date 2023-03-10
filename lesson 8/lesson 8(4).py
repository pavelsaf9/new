import time

def countdown_timer(num):
    if num < 10 or num > 30:
        print("Ошибка! Введите число от 10 до 30.")
    else:
        for i in range(num, -1, -1):
            print(i, end="", flush=True)
            time.sleep(1)
            print("\b", end="", flush=True)
        print("\n" + "Отсчет завершен.")

countdown_timer(10)

