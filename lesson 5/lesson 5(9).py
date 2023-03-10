target_ints = (1, 3, 3, 4, 7, 9)
count = []

for i in target_ints:
    if target_ints.count(i) == 2:
        count.append(i)
print(count)