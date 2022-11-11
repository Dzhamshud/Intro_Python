# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')

def draw(player1, player2):  # Жеребьевка
    print('Жеребьевка.')
    print('Введите число от 1 до 10, тот чье число будет ближе к загаданному, начинает первым.')
    draw_player1 = int(input(f'{player1} введите число от 1 до 10: '))
    draw_player2 = int(input(f'{player2} введите число от 1 до 10: '))
    flag_draw = False
    while flag_draw == False:
        draw = randint(1, 10)
        if abs(draw-draw_player1)>abs(draw-draw_player2):
            flag_draw = True
            print(f'Загаданное число {draw}, поэтому {player2} делает ход первым')
            return -1
        elif abs(draw-draw_player1)<abs(draw-draw_player2):
            flag_draw = True
            print(f'Загаданное число {draw}, поэтому {player1} делает ход первым')
            return 0
        else:
            continue

def play(player1, player2, total):  # Игра двух игроков друг с другом
    print(f'Всего есть {total} конфет(а), выигрывает тот кто забирёт последние.')
    while total>0:
        move_player1 = int(input(f'{player1} введите число от 1 до 28: '))
        if 1<=move_player1<=28:
            total = total - move_player1
            print(f'Осталось {total} конфет')
            if total <=0:
                print(f'Игрок {player1} победил!')
                break
        else:
            print('Введите корректное число! Переход хода.')
        move_player2 = int(input(f'{player2} введите число от 1 до 28: '))
        if 1<=move_player2<=28:
            total = total - move_player2
            print(f'Осталось {total} конфет')
            if total <=0:
                print(f'Игрок {player2} победил!')
                break
        else:
            print('Введите корректное число! Переход хода.')

def play_bot(total):  # Игра с ботом
    print(f'Всего есть {total} конфет(а), выигрывает тот кто забирёт последние.')
    while total>0:
        move_player = int(input('Ход игрока. Введите число от 1 до 28: '))
        if 1<=move_player<=28:
            total = total - move_player
            print(f'Осталось {total} конфет')
            if total <=0:
                print('Игрок победил!')
                break
        else:
            print('Введите корректное число! Переход хода.')
            continue
        if total//28 >0 and total !=28:
            move_bot = int((total-29)%28)
            if 1<=move_bot<=28:
                total -= move_bot
                print(f'Ход бота равен {move_bot}')
                print(f'Осталось {total} конфет')
            else:
                move_bot = 28
                total -= move_bot
                print(f'Ход бота равен {move_bot}')
                print(f'Осталось {total} конфет')
        else:
            if total <29:
                move_bot = total
                total -= move_bot
                print(f'Ход бота равен {move_bot}')
                print(f'Осталось {total} конфет')
                print('Бот победил!')
                break
            else:
                move_bot = 28
                total -= move_bot
                print(f'Ход бота равен {move_bot}')
                print(f'Осталось {total} конфет')

def play_bot_new(total):  # Игра с ботом, где бот всегда выигрывает
    print(f'Всего есть {total} конфет(а), выигрывает тот кто забирёт последние.')
    move_bot_first = total%29
    total -= move_bot_first
    print(f'Ход бота равен {move_bot_first}')
    print(f'Осталось {total} конфет')
    while total>0:
        move_player = int(input('Ход игрока. Введите число от 1 до 28: '))
        if 1<=move_player<=28:
            total = total - move_player
            print(f'Осталось {total} конфет')
            if total <=0:
                print('Игрок победил!')
                break
        else:
            print('Введите корректное число! Переход хода.')
            continue
        if total>29:
            move_bot = int(29-move_player)
            total -= move_bot
            print(f'Ход бота равен {move_bot}')
            print(f'Осталось {total} конфет')
        else:
            if total <29:
                move_bot = total
                total -= move_bot
                print(f'Ход бота равен {move_bot}')
                print(f'Осталось {total} конфет')
                print('Бот победил!')
                break


if draw(name1, name2) !=0:
    name2, name1 = name1, name2
play(name1, name2, 2021)
# play_bot(121)
play_bot_new(250)

