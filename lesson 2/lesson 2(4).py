height_home = 3
length_for_home = 4
add_rope = 1.5

sum_rope = add_rope + add_rope  # На каждый конец веревки добавляется по 1.5м
rope_length = ((height_home**2 + length_for_home**2)**0.5) + sum_rope

print("Понадобиться", rope_length, "метров верёвки")
