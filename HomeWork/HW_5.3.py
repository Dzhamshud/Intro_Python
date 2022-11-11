# Создайте программу для игры в ""Крестики-нолики"".

name1 = input('Введите имя первого игрока: ')
symbol1 = 'x'
name2 = input('Введите имя первого игрока: ')
symbol2 = 'o'
print(f'{name1} играет за {symbol1} и ходит первым')
print(f'{name2} играет за {symbol2} и ходит вторым')
win = False

moves = ['-' for i in range(9)]
journal_moves = []

def print_game(moves_players):  # Печать поля
    print(f"""       A   B   C
    1 _{moves_players[0]}_|_{moves_players[1]}_|_{moves_players[2]}_
    2 _{moves_players[3]}_|_{moves_players[4]}_|_{moves_players[5]}_
    3  {moves_players[6]} | {moves_players[7]} | {moves_players[8]} """)

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

def check_win(name, moves_players, symbol):  # Проверяем выигрыш
    if (moves[0] == moves[1] == moves[2] == symbol or
        moves[3] == moves[4] == moves[5] == symbol or
        moves[6] == moves[7] == moves[8] == symbol or
        moves[0] == moves[4] == moves[8] == symbol or
        moves[2] == moves[4] == moves[6] == symbol or
        moves[0] == moves[3] == moves[6] == symbol or
        moves[1] == moves[4] == moves[7] == symbol or
        moves[2] == moves[5] == moves[8] == symbol):
        return True
    else:
        return False

print_game(moves)
counter = 0
while win == False:
    if counter >8:
        win == True
        print('Ничья!')
        break
    move_player1 = move_players(name1, symbol1)
    moves.pop(move_player1)
    moves.insert(move_player1, symbol1)
    print_game(moves)
    win = check_win(name1, moves, symbol1)
    counter +=1
    if win == True:
        print(f'{name1} победил!')
        break
    if counter >8:
        win == True
        print('Ничья!')
        break
    move_player2 = move_players(name2, symbol2)
    moves.pop(move_player2)
    moves.insert(move_player2, symbol2)
    print_game(moves)
    win = check_win(name2, moves, symbol2)
    counter +=1
    if win == True:
        print(f'{name2} победил!')
        break


