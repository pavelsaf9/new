print("fanat > apple", "fanat" > "apple")
print("fanat > abracadabra", "fanat" > "abracadabra")
print("fanat > Tarantino", "fanat" > "Tarantino")
print("fanat > yahoo", "fanat" > "yahoo")
print("yahoo > yandex", "yahoo" > "yandex")
print("yandex > gool", "yandex" > "gool")
print("yandex > logo", "yandex" > "logo")
# yandex является самым большим словом, при сравнении строк Python
# конвертирует символы в их порядковые номера по таблице ASCII
# после чего сравнивает значения слева направо
# например символ 'y' > 'l' т.к значение Unicode y = 121 больше, чем l = 108
