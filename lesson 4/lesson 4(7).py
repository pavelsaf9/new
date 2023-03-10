hour, minute = input('Введите время: ').split(':')
hour_in_minute = (int(hour)*60 + int(minute))

if not 360 <= hour_in_minute <= 1080:
    print('Солнце за горизонтом!')
else:
    angle = (hour_in_minute - 360)/((12*60)/180)
    print('Угол солнца', angle, 'градусов')
