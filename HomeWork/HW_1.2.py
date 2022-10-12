# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

diap = [0, 1]
flag = False
for x in range(2):  # 1-й способ
    for y in [0, 1]:  # 2-й способ
        for z in diap:  # 3-й способ
            if (not(x or y or z)) == (not(x) and not(y) and not(z)):
                flag = True
            else:
                flag = False
            print(x, y, z, flag)
