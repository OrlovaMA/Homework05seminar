# Задача 2.
# Создайте программу для игры в 'Крестики-нолики'
# Игра с ботом 

import random 
gamer_1 = 'Игрок'

print('\nПервый ход твой, Игрок!')

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# вывод игрового поля
def print_field():
    print(field[0], end=' ')
    print(field[1], end=' ')
    print(field[2])
    print(field[3], end=' ')
    print(field[4], end=' ')
    print(field[5])
    print(field[6], end=' ')
    print(field[7], end=' ')
    print(field[8])

# победные комбинации
win_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

# проверка, кто победил
def wincheck():
    winner = ''
    for i in win_combinations:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            winner = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            winner = 'O'   
    return winner

# функция обрабатывает ход игрока
def steps(cell_1, symbol_1):
    while True:
        cell_1 = int(input('Твой ход: '))
        if cell_1 in field:
            s1 = field.index(cell_1)
            field[s1] = symbol_1
            print_field()
            break
        if cell_1 not in field:
            print('Эта клетка уже сыграла, сделай другой ход: ')

# игра
count_cell = 0
while count_cell <10:
    count_cell = 0
    symbol_1 = 'X'
    cell_1 = ''
    steps(cell_1, symbol_1)
    count_cell += 1
    winner = wincheck()
    
    if winner == 'X' or winner == 'O':
        print('Выиграл', 'Бот' if winner == 'O' else 'Игрок!')
        break
            
    if count_cell == 9:
        if winner != 'X' and winner != 'O':
            print('Ничья!')
        break
               
    for i in field:
        move2 = random.randint(0, 8)
        if type(field[move2]) == int:
            field[move2] = 'O'
            print('Бот сделал ход:')
            print_field()
            break
        else:
            continue
    count_cell += 1
    winner = wincheck()
    if winner == 'X' or winner == 'O':
        print('Выиграл', 'Бот' if winner == 'O' else 'Игрок')
        break
            
    if count_cell == 9:
        if winner != 'X' and winner != 'O':
            print('Ничья!')
            break