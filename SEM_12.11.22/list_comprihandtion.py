my_list = []
for i in range(1, 101):
    if i%3 == 0:
        my_list.append(i)
print(my_list)

my_list1 = [i for i in range(1, 101) if i%3 == 0]
print(my_list1)

my_list2 = [i for i in my_list1 if 10 < i < 30]
print(my_list2)


# лист комприхендшен для словаря
names = ['Tom', 'Peter', 'Irina', 'Pavel']
ages = [44, 33, 66, 22, 99, 88]

dct = {name: age for name, age in zip(names, ages)}
print(dct)

my_dict = {age: name for name, age in dct.items()}
print(my_dict)


print([x+y for x in [1, 2] for y in [10, 20]])  # двойной цикл применения лист комприхендшен (сложение двух чисел x + y)

matrix = []
for i in range(3):
    temp = []
    for j in range(1, 4):
        temp.append(j+3*i)
    matrix.append(temp)
print(matrix)

matrix_new =[[(j+3*i) for j in range(1, 4)] for i in range(3)] # лист комприхендшен заполнение матрицы
print(matrix_new)

print(matrix_new[1][1])
print([[string[i] for string in matrix_new] for i in range(3)])

