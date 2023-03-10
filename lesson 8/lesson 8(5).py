from lorem_text import lorem
import time
from colorama import *


def greeting(countdown):
    for i in range(countdown, 0, -1):
        print(i, end='... ')
        time.sleep(1)

    print(Fore.RED + 'Начали')


def random_string():
    words = lorem.words(count=5)
    print(Fore.LIGHTCYAN_EX + words, Style.RESET_ALL)
    print()
    start_time = time.time()
    input_text = input('Введите текст выше: ')
    end_time = time.time()
    time_elapsed = end_time - start_time
    typing_speed = round(len(words) / time_elapsed, 2)

    if input_text == words:
        print()
        print(Fore.LIGHTGREEN_EX + '###################################')
        print(Fore.LIGHTGREEN_EX + '###### Вы отлично справились! #####')
        print(Fore.LIGHTGREEN_EX + '###### Время печати:',
              round(time_elapsed, 2),'с.', '######')
        print(Fore.LIGHTGREEN_EX + '### Скорость печати:',
              typing_speed,'зн/м', '####')
        print(Fore.LIGHTGREEN_EX + '###################################')
    else:
        print("Ошибка: набранный текст не соответствует заданной строке")


greeting(3)
print()
random_string()
