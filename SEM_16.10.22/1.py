# Программа перевода десятиричного числа в двоичное

a = int(input('Введите десятиричное число: '))
num_bin = ''
while a > 0:
    ost = a % 2
    num_bin = str(ost) + num_bin
    a = a // 2
print(num_bin)


a = 14
print(bin(a)[2:])  # подпрограмма перевода десятиричного числа в двоичное, с функцией среза строки начиная со второго символа