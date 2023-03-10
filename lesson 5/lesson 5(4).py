jewels = ('золото', 'алмазы', 'серебро', 'сапфиры', 'бронза',
          'рубины', 'платина', 'изумруды', 'палладий', 'аметисты')

for index, value in enumerate(jewels):
    for index, value in enumerate(jewels[::2]):
        print(index, value)

# jewels = ('золото', 'алмазы', 'серебро', 'сапфиры', 'бронза',
#           'рубины', 'платина', 'изумруды', 'палладий', 'аметисты')
#
# for index, value in enumerate(jewels[0::2]):
#     index += 1
#     print(index, value)
# print()
# for index, value in enumerate(jewels[1::2]):
#     index += 1
#     print(index, value)
