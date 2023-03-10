def calculate_time_to_shoot_all_bullets(num_bullets):
    if num_bullets < 250 or num_bullets > 10000:
        print("Введите число от 250 до 10000.")
        return None
    else:
        num_belts = (num_bullets - 1) // 250 + 1  # количество лент
        shooting_time = (num_belts - 1) * 20  # время на смену лент
        shooting_time += num_bullets / 1200 * 60  # время на стрельбу
        return shooting_time


num_bullets = int(input("Введите количество патронов: "))
time_to_shoot = calculate_time_to_shoot_all_bullets(num_bullets)
if time_to_shoot:
    print("Пулемётчик расстреляет все патроны за", time_to_shoot, "секунд.")
