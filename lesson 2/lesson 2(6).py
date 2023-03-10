pedestrian_speed = 4
time_pedestrian = 2
hour = 60
speed = 3.6


car_time = 10/hour  # Переводим минуты в часы
car_speed = 30*speed  # Переводим м/сек в км/ч
car_distance = car_speed*car_time
walking_distance = (car_distance/pedestrian_speed) - time_pedestrian


print("Пешеход прошел от точки А:", time_pedestrian, "часа")
print("И достигнет точки Б через:", walking_distance, "часов")