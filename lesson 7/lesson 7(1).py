import string
import random


def generete_random_string(lenght):
    symbols = string.ascii_letters + string.digits
    print('Список случайных 10 символов:',
          random.sample(symbols, lenght), sep='\n')
    print('Список случайных 10 символов:',
          random.choices(symbols, k=lenght), sep='\n')
    print('Список случайных 10 символов:',
          [symbols[random.randint(0, len(symbols)-1)]
           for _ in range(10)], sep='\n')


generete_random_string(10)
