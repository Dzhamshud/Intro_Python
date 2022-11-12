names = ['Tom', 'Peter', 'Irina', 'Pavel']
ages = [44, 33, 66, 22, 99, 88]

for i in range(4):
    print(names[i], ages[i])
print()
for name, age in zip(names, ages):
    print(name, age)
print()
for i in zip(names, ages):
    print(i)
    print(i[0])
