target_dict = {'o': 3, 'd': 7, 'k': 5, 'w': 2, 'e': 6, 'g': 1, 'y': 4}

print(''.join(target_dict.keys())[::2])
print('Сумма значений словаря:', sum(target_dict.values()))
print('Отсортированный список значений:', sorted(target_dict.values()))
print('Сумма третьих значений словаря:', sum(tuple(target_dict.values())[::3]))
