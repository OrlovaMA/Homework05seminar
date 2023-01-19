# Задача 1.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Игра против бота.

from random import randint

gamer_1 = input('\nВведите имя игрока: ')
gamer_2 = 'Бот'
candies = (input(gamer_1 + ', сколько конфет будет в игре? '))
candies = int(candies)
print(f'В игре {candies} конфет')
print('\nРазыграем первый ход,' + gamer_1 + '!')

# розыгрыш первого хода
move = randint(0,2) 
if move == 0:
    print('\nПервый ход твой,' + gamer_1 +'!')
else:
    print('\nПервый ход у Бота')

# игра
while candies > 0:
    if move == 0:
        while candies > 28:
            c_1 = int(input(gamer_1 + ', сколько возьмёшь конфет (от 1 до 28): '))
            while c_1 < 1 or c_1 > 28:
                c_1 = int(input(gamer_1 + ', можно взять от 1 до 28 конфет: '))
            if 1 <= c_1 <=28:
                candies -= c_1
                print('\nОсталось ' + str(candies) + ' конфет')
            if candies <= 28:
                print('Последние ' + str(candies) + ' конфет забирает Бот')
                print('Игра окончена!!! Выиграл Бот!')
                break
            c_2 = int(randint(1,28))
            candies -= c_2
            print('Бот взял ' + str(c_2) + ' конфет. Осталось ' + str(candies) + ' конфет')
            if candies <= 28:
                print('Последние ' + str(candies) + ' конфет забирает ' + gamer_1)
                print('Игра окончена, поздравляю, ' + gamer_1 + '!!! Ты выиграл!')
                break
    else: 
        while candies > 28:
            c_2 = int(randint(1,28))
            candies -= c_2
            print('\nБот взял ' + str(c_2) + ' конфет. Осталось ' + str(candies) + ' конфет')
            if candies <= 28:
                print('\nПоследние ' + str(candies) + ' конфет забирает ' + gamer_1)
                print('Игра окончена, поздравляю,' + gamer_1 + '!!! Ты выиграл!')
                break

            c_1 = int(input(gamer_1 + ', сколько возьмёшь конфет (от 1 до 28): '))
            while c_1 < 1 or c_1 > 28:
                c_1 = int(input(gamer_1 + ', можно взять от 1 до 28 конфет: '))
            candies -= c_1
            print('\nОсталось ' + str(candies) + ' конфет')
            
            if candies <= 28:
                print('Последние ' + str(candies) + ' конфет забирает Бот')
                print('Игра окончена!!! Выиграл Бот!')
                break
