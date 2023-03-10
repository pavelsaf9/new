hour = int(input('Введите часы: '))
minutes = int(input('Введите минуты: '))
seconds = int(input('Введите секунды: '))

if not 0 <= hour <= 23 or not 0 <= minutes <= 59 or not 0 <= seconds <= 59:
    print("Введите числа для часов от 0 до 23 и для минут и секунд от 0 до 59")
else:
    if hour <= 9:
        hour = '0' + str(hour)
    if minutes <= 9:
        minutes = '0' + str(minutes)
    if seconds <= 9:
        seconds = '0' + str(seconds)
    print(hour, minutes, seconds, sep=':')
