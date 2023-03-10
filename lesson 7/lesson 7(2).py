import example as s
from colorama import*

colors = {
    ':': Fore.LIGHTWHITE_EX,
    "'": Fore.LIGHTWHITE_EX,
    '.': Fore.LIGHTWHITE_EX,
    '#': Fore.LIGHTGREEN_EX
}

for char in s.str_examp:
    print(colors.get(char, '') + char, end='')


