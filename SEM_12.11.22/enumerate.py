names = ['Tom', 'Peter', 'Irina', 'Pavel']
ages = [44, 33, 66, 22, 99, 88]

for index, (name, age) in enumerate(zip(names, ages)):
    print(index, name, age)
print()
my_dict = {'Tom': 44, 'Peter': 33}  # словарь
print(my_dict['Tom'])