botnet = 1000
lost_botnet = 2
new_botnet = 3
in_day = 30

print("Через 30 дней, по -2 бота. Будет:", botnet - (in_day * lost_botnet))
print("Через 30 дней, по + 3 бота. Будет:", botnet + (in_day * new_botnet))
