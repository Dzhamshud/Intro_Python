# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
a = [1, 3, 5, 6]  # список
# a = list()  # 2-й спопосб инициализации списка
a[3] = 8
print(a)

# инициализация словаря, отличие от списка в том что индексация элементов задается программно по желанию
b = {3: 17, 8: 22, 'c': 10}
# b = dict() 2-й способ инициализации словаря
b[3] = 22
b['c'] = 'list'
print(b)

# переводчик фразы
my_dict = {
    'dog': 'собака',
    'cat': 'кошка',
    'is': 'есть',
    'good': 'хорошая'
}

eng_text = 'dog is good'
rus_text = ''
for word in eng_text.split():
    if word in eng_text:
        rus_text = rus_text + my_dict[word]
        rus_text = rus_text + ' '
print(rus_text)
