targets = ["7 раз отмерь, 1 раз отрежь.",
           "Не имей 100 рублей, а имей 100 друзей.", "1 за всех и все за 1 ."]

for target in targets:
    count = 0
    for x in target.split():
        if x.isdigit():
            count += int(x)
    print(target, count)
