# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# txt = input('Введите текст через пробел: ')
# print(f'Исходный текст: {txt}')
# lst = [i for i in txt.split() if 'абв' not in i]
# print(f'Результат: {" ".join(lst)}') # формирует из некоторого количества строк одну строку, в конкретном случае разделенную пробелом(" ".join(lst))

player1 = 'x'
player2 = 'o'
name1 = 'Павел'

moves = ['-' for i in range(9)]
moves.insert(0, player1)


def print_game(moves_players):
    print(f"""   A   B   C
    1 _{moves_players[0]}_|_{moves_players[1]}_|_{moves_players[2]}_
    2 _{moves_players[3]}_|_{moves_players[4]}_|_{moves_players[5]}_
    3  {moves_players[6]} | {moves_players[7]} | {moves_players[8]} """)

print_game(moves)
def move_players(name, symbol):  # Ход игрока
    move_player = input(f'{name} введите координаты ячейки для "{symbol}": ')
    if (move_player == 'A1' or move_player == '1A' or move_player == 'a1' or
        move_player == '1a' or move_player == 'А1' or move_player == '1А' or
        move_player == 'а1' or move_player == '1а'):
        return 0
    elif (move_player == 'B1' or move_player == '1B' or move_player == 'b1' or
          move_player == '1b' or move_player == 'В1' or move_player == '1В' or
          move_player == 'в1' or move_player == '1в'):
        return 1
    elif (move_player == 'C1' or move_player == '1C' or move_player == 'c1' or
          move_player == '1c' or move_player == 'С1' or move_player == '1С' or
          move_player == 'с1' or move_player == '1с'):
        return 2
    elif (move_player == 'A2' or move_player == '2A' or move_player == 'a2' or
          move_player == '2a' or move_player == 'А2' or move_player == '2А' or
          move_player == 'а2' or move_player == '2а'):
        return 3
    elif (move_player == 'B2' or move_player == '2B' or move_player == 'b2' or
          move_player == '2b' or move_player == 'В2' or move_player == '2В' or
          move_player == 'в2' or move_player == '2в'):
        return 4
    elif (move_player == 'C2' or move_player == '2C' or move_player == 'c2' or
          move_player == '2c' or move_player == 'С2' or move_player == '2С' or
          move_player == 'с2' or move_player == '2с'):
        return 5
    elif (move_player == 'A3' or move_player == '3A' or move_player == 'a3' or
          move_player == '3a' or move_player == 'А3' or move_player == '3А' or
          move_player == 'а3' or move_player == '3а'):
        return 6
    elif (move_player == 'B3' or move_player == '3B' or move_player == 'b3' or
          move_player == '3b' or move_player == 'В3' or move_player == '3В' or
          move_player == 'в3' or move_player == '3в'):
        return 7
    elif (move_player == 'C3' or move_player == '3C' or move_player == 'c3' or
          move_player == '3c' or move_player == 'С3' or move_player == '3С' or
          move_player == 'с3' or move_player == '3с'):
        return 8
    else:
        print('Введите корректное значение. Переход хода.')

index = move_players(name1, player1)
print(index)


