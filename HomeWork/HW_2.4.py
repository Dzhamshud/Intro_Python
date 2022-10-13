# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число '))
my_list = []
for elem in range(-n, n+1):
    my_list.append(elem)
print(my_list)

data = open('file.txt', 'w')
data.write(input(f'Введите номер 1-й позиции элемента от -{n} до {n} '))
data.write('\n')
data = open('file.txt', 'a')
data.write(input(f'Введите номер 2-й позиции элемента от -{n} до {n} '))
data.close()

lst = []
path = 'file.txt'
data = open(path, 'r')
for line in data:
    for i in range(1):
        lst.append(line)
data.close()

print('Произведение элементов равно', int(lst[0])*int(lst[1]))
