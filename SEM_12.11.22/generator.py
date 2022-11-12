def my_range(n):  # метод создания генератора my_range со значениями [1, n] вместо стандартного range со сзначениями [0, n)
    i = 0
    while i<n:
        i += 1
        yield i  # возвращает значение как return, но не останавливает выполнение метода

for i in my_range(10):
    print(i)



def my_div(n):  # метод генератора чисел кратных 3
    i = 0
    while i<n:
        yield i
        i += 3

my_list = [i for i in my_div(50)]
print(my_list)

my_gen = (i for i in range(100) if '9' in str(i))  # лист комприхендшен создания генератора чисел в которых содержиться цифра 9
print(sum(my_gen))
