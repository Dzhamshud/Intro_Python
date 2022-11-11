# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

koefs = []
k = int(input('Какая степень многочлена? '))

# for i in range(k+1):
#     num = randint(-10, 10)
#     koefs.append(num)
koefs = [randint(-10, 10) for _ in range(k+1)]  # задействовали функцию лист комприхендшн(list comprehansion)
print(koefs)
result = ''

# for i in range(len(koefs)):  # используется koefs[i]
for i, koef in enumerate(koefs):  # задействовали функцию енумирейт(enumerate)
    if len(result)>0 and koef>0:
        result = result + '+'
    if koef == 0:
        continue
    result = result + str(koef) + 'x^' + str(k-i)
if koef != 0:
    result = result[:len(result)-3]
result = result + ' = 0'
print(result)

with open('file.txt', 'w') as f:
    f.write(result)

