my_dict = {1: ("прокоп", "порок"), 2: ("сушилка", "осушка"),
           3: ("вязанка", "навязка"), 4: ("каторга", "рогатка"),
           5: ("плесень", "полдник")}

new_turple = my_dict[1]
new_turple_1 = my_dict[2]
new_turple_2 = my_dict[3]
new_turple_3 = my_dict[4]
new_turple_4 = my_dict[5]

print(*new_turple, new_turple[0][0] == new_turple[1][0])
print(*new_turple_1, new_turple_1[0][0] == new_turple_1[1][0])
print(*new_turple_2, new_turple_2[0][0] == new_turple_2[1][0])
print(*new_turple_3, new_turple_3[0][0] == new_turple_3[1][0])
print(*new_turple_4, new_turple_4[0][0] == new_turple_4[1][0])
