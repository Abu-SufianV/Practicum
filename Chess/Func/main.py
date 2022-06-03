import art
from random import randint
from time import sleep
from datetime import datetime


def greeting(persons: list, first: int) -> None:
    """
    Приветствие; запрос имён у игроков; определение игрока, начинающего партию
    """

    print('\033[34m')
    art.tprint('CHESS')

    print("Добро пожаловать в наш небольшой шахматный мир!\n"
          "Пожалуйста, представьтесь")

    print('\033[32m')
    name = input('Игрок 1: ')
    if name != '':
        persons[0] = name

    print('\033[33m')
    name = input('Игрок 2: ')
    if name != '':
        persons[1] = name
    print('\033[39m')

    print("ОТЛИЧНО!\n"
          "Теперь 'подбросим монетку' для определения того,\n"
          "кто будет играть за белые фигуры", end='')
    for _ in range(3):
        sleep(1)
        print(' .', end='')

    # Проходит жеребьёвка, после которой определяется игрок начинающий партию
    num = randint(0, 2)
    print('\n')
    sleep(1)
    if num == 1:
        print(f'Партию начинает - \033[32m{persons[0]}\n\033[39m')
    else:
        first += 1
        print(f'Партию начинает - \033[33m{persons[1]}\n\033[39m')

    sleep(2)
    art.tprint("Let's      start!")
    sleep(1)

    return


def desk_show(board: list) -> None:
    """
    Выводит шахматную доску в терминал
    """
    for row in board:
        print(*row)


def get_color(board: list, x: int, y: int) -> int:
    if board[x][y].strip() == '.':
        return COLOR['empty']
    if board[x][y].strip().islower():
        return COLOR['black']
    return COLOR['white']


def get_moves_pawn(board: list, x: int, y: int) -> list:
    possible_moves = []
    color = get_color(board, x, y)

    # Проверка для чёрных фигур
    if color == COLOR['black'] \
            and x == 2 \
            and get_color(board, x + 1, y) == COLOR['empty'] \
            and get_color(board, x + 2, y) == COLOR['empty']:
        possible_moves.append([x + 1, y])
        possible_moves.append([x + 2, y])
    elif color == COLOR['black'] \
            and x >= 2 \
            and get_color(board, x + 1, y) == COLOR['empty']:
        possible_moves.append([x + 1, y])

    # Проверка для белых фигур
    if color == COLOR['white'] \
            and x == 7 \
            and get_color(board, x - 1, y) == COLOR['empty'] \
            and get_color(board, x - 2, y) == COLOR['empty']:
        possible_moves.append([x - 1, y])
        possible_moves.append([x - 2, y])
    elif color == COLOR['white'] \
            and x <= 7 \
            and get_color(board, x - 1, y) == COLOR['empty']:
        possible_moves.append([x - 1, y])

    return possible_moves


def get_moves_king(board: list, x: int, y: int):
    possible_moves = []
    color = get_color(board, x, y)

    if color == COLOR['white']:

        if get_color(board, x - 1, y) != COLOR['white']:
            possible_moves.append([x - 1, y])

        if get_color(board, x + 1, y) != COLOR['white']:
            possible_moves.append([x + 1, y])

        if get_color(board, x - 1, y - 1) != COLOR['white']:
            possible_moves.append([x - 1, y - 1])

        if get_color(board, x - 1, y + 1) != COLOR['white']:
            possible_moves.append([x - 1, y + 1])

        if get_color(board, x + 1, y - 1) != COLOR['white']:
            possible_moves.append([x + 1, y - 1])

        if get_color(board, x + 1, y + 1) != COLOR['white']:
            possible_moves.append([x + 1, y + 1])

        if get_color(board, x, y - 1) != COLOR['white']:
            possible_moves.append([x, y - 1])

        if get_color(board, x, y + 1) != COLOR['white']:
            possible_moves.append([x, y + 1])

    # Проверка для чёрных фигур
    if color == COLOR['black']:

        if get_color(board, x - 1, y) != COLOR['black']:
            possible_moves.append([x - 1, y])

        if get_color(board, x + 1, y) != COLOR['black']:
            possible_moves.append([x + 1, y])

        if get_color(board, x - 1, y - 1) != COLOR['black']:
            possible_moves.append([x - 1, y - 1])

        if get_color(board, x - 1, y + 1) != COLOR['black']:
            possible_moves.append([x - 1, y + 1])

        if get_color(board, x + 1, y - 1) != COLOR['black']:
            possible_moves.append([x + 1, y - 1])

        if get_color(board, x + 1, y + 1) != COLOR['black']:
            possible_moves.append([x + 1, y + 1])

        if get_color(board, x, y - 1) != COLOR['black']:
            possible_moves.append([x, y - 1])

        if get_color(board, x, y + 1) != COLOR['black']:
            possible_moves.append([x, y + 1])

    return possible_moves


def get_moves_queen(board: list, x: int, y: int):
    possible_moves = []
    color = get_color(board, x, y)

    # Проверка для белых фигур по вертикали/горизонтали
    if color == COLOR['white']:

        for i in range(1, 9 - x):
            if get_color(board, x + i, y) == COLOR['empty']:
                possible_moves.append([x + i, y])
            elif get_color(board, x + i, y) == COLOR['black']:
                possible_moves.append([x + i, y])
                break
            elif get_color(board, x + i, y) == COLOR['white']:
                break

        for i in range(1, x):
            if get_color(board, x - i, y) == COLOR['empty']:
                possible_moves.append([x - i, y])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x - i, y])
                break
            elif get_color(board, x - i, y) == COLOR['white']:
                break

        for i in range(1, 9 - y):
            if get_color(board, x, y + i) == COLOR['empty']:
                possible_moves.append([x, y + i])
            elif get_color(board, x, y + i) == COLOR['black']:
                possible_moves.append([x, y + i])
                break
            elif get_color(board, x, y + i) == COLOR['white']:
                break

        for i in range(1, y):
            if get_color(board, x, y - i) == COLOR['empty']:
                possible_moves.append([x, y - i])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x, y - i])
                break
            elif get_color(board, x, y - i) == COLOR['white']:
                break

        # Проверка для белых фигур по диагоналям
        for i in range(1, 9):
            try:
                if get_color(board, x + i, y + i) == COLOR['empty']:
                    possible_moves.append([x + i, y + i])
                elif get_color(board, x + i, y + i) == COLOR['black']:
                    possible_moves.append([x + i, y + i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y - i) == COLOR['empty']:
                    possible_moves.append([x + i, y - i])
                elif get_color(board, x + i, y - i) == COLOR['black']:
                    possible_moves.append([x + i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y - i) == COLOR['empty']:
                    possible_moves.append([x - i, y - i])
                elif get_color(board, x - i, y - i) == COLOR['black']:
                    possible_moves.append([x - i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y + i) == COLOR['empty']:
                    possible_moves.append([x - i, y + i])
                elif get_color(board, x - i, y + i) == COLOR['black']:
                    possible_moves.append([x - i, y + i])
                    break
                else:
                    break
            except Exception:
                break
    # Проверка для чёрных фигур по вертикали/горизонтали
    if color == COLOR['black']:

        for i in range(1, 9 - x):
            if get_color(board, x + i, y) == COLOR['empty']:
                possible_moves.append([x + i, y])
            elif get_color(board, x + i, y) == COLOR['black']:
                possible_moves.append([x + i, y])
                break
            elif get_color(board, x + i, y) == COLOR['white']:
                break

        for i in range(1, x):
            if get_color(board, x - i, y) == COLOR['empty']:
                possible_moves.append([x - i, y])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x - i, y])
                break
            elif get_color(board, x - i, y) == COLOR['white']:
                break

        for i in range(1, 9 - y):
            if get_color(board, x, y + i) == COLOR['empty']:
                possible_moves.append([x, y + i])
            elif get_color(board, x, y + i) == COLOR['black']:
                possible_moves.append([x, y + i])
                break
            elif get_color(board, x, y + i) == COLOR['white']:
                break

        for i in range(1, y):
            if get_color(board, x, y - i) == COLOR['empty']:
                possible_moves.append([x, y - i])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x, y - i])
                break
            elif get_color(board, x, y - i) == COLOR['white']:
                break

        # Проверка для чёрных фигур по диагоналям
        for i in range(1, 9):
            try:
                if get_color(board, x + i, y + i) == COLOR['empty']:
                    possible_moves.append([x + i, y + i])
                elif get_color(board, x + i, y + i) == COLOR['white']:
                    possible_moves.append([x + i, y + i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y - i) == COLOR['empty']:
                    possible_moves.append([x + i, y - i])
                elif get_color(board, x + i, y - i) == COLOR['white']:
                    possible_moves.append([x + i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y - i) == COLOR['empty']:
                    possible_moves.append([x - i, y - i])
                elif get_color(board, x - i, y - i) == COLOR['white']:
                    possible_moves.append([x - i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y + i) == COLOR['empty']:
                    possible_moves.append([x - i, y + i])
                elif get_color(board, x - i, y + i) == COLOR['white']:
                    possible_moves.append([x - i, y + i])
                    break
                else:
                    break
            except Exception:
                break

    return possible_moves


def get_moves_rook(board: list, x: int, y: int):
    possible_moves = []
    color = get_color(board, x, y)

    # Проверка для белых фигур
    if color == COLOR['white']:

        for i in range(1, 9 - x):
            if get_color(board, x + i, y) == COLOR['empty']:
                possible_moves.append([x + i, y])
            elif get_color(board, x + i, y) == COLOR['black']:
                possible_moves.append([x + i, y])
                break
            elif get_color(board, x + i, y) == COLOR['white']:
                break

        for i in range(1, x):
            if get_color(board, x - i, y) == COLOR['empty']:
                possible_moves.append([x - i, y])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x - i, y])
                break
            elif get_color(board, x - i, y) == COLOR['white']:
                break

        for i in range(1, 9 - y):
            if get_color(board, x, y + i) == COLOR['empty']:
                possible_moves.append([x, y + i])
            elif get_color(board, x, y + i) == COLOR['black']:
                possible_moves.append([x, y + i])
                break
            elif get_color(board, x, y + i) == COLOR['white']:
                break

        for i in range(1, y):
            if get_color(board, x, y - i) == COLOR['empty']:
                possible_moves.append([x, y - i])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x, y - i])
                break
            elif get_color(board, x, y - i) == COLOR['white']:
                break

    # Проверка для чёрных фигур
    if color == COLOR['black']:

        for i in range(1, 9 - x):
            if get_color(board, x + i, y) == COLOR['empty']:
                possible_moves.append([x + i, y])
            elif get_color(board, x + i, y) == COLOR['black']:
                possible_moves.append([x + i, y])
                break
            elif get_color(board, x + i, y) == COLOR['white']:
                break

        for i in range(1, x):
            if get_color(board, x - i, y) == COLOR['empty']:
                possible_moves.append([x - i, y])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x - i, y])
                break
            elif get_color(board, x - i, y) == COLOR['white']:
                break

        for i in range(1, 9 - y):
            if get_color(board, x, y + i) == COLOR['empty']:
                possible_moves.append([x, y + i])
            elif get_color(board, x, y + i) == COLOR['black']:
                possible_moves.append([x, y + i])
                break
            elif get_color(board, x, y + i) == COLOR['white']:
                break

        for i in range(1, y):
            if get_color(board, x, y - i) == COLOR['empty']:
                possible_moves.append([x, y - i])
            elif get_color(board, x - i, y) == COLOR['black']:
                possible_moves.append([x, y - i])
                break
            elif get_color(board, x, y - i) == COLOR['white']:
                break

    return possible_moves


def get_moves_bishop(board: list, x: int, y: int):
    possible_moves = []
    color = get_color(board, x, y)

    if color == COLOR['white']:

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y + i) == COLOR['empty']:
                    possible_moves.append([x + i, y + i])
                elif get_color(board, x + i, y + i) == COLOR['black']:
                    possible_moves.append([x + i, y + i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y - i) == COLOR['empty']:
                    possible_moves.append([x + i, y - i])
                elif get_color(board, x + i, y - i) == COLOR['black']:
                    possible_moves.append([x + i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y - i) == COLOR['empty']:
                    possible_moves.append([x - i, y - i])
                elif get_color(board, x - i, y - i) == COLOR['black']:
                    possible_moves.append([x - i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y + i) == COLOR['empty']:
                    possible_moves.append([x - i, y + i])
                elif get_color(board, x - i, y + i) == COLOR['black']:
                    possible_moves.append([x - i, y + i])
                    break
                else:
                    break
            except Exception:
                break

    if color == COLOR['black']:

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y + i) == COLOR['empty']:
                    possible_moves.append([x + i, y + i])
                elif get_color(board, x + i, y + i) == COLOR['white']:
                    possible_moves.append([x + i, y + i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x + i, y - i) == COLOR['empty']:
                    possible_moves.append([x + i, y - i])
                elif get_color(board, x + i, y - i) == COLOR['white']:
                    possible_moves.append([x + i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y - i) == COLOR['empty']:
                    possible_moves.append([x - i, y - i])
                elif get_color(board, x - i, y - i) == COLOR['white']:
                    possible_moves.append([x - i, y - i])
                    break
                else:
                    break
            except Exception:
                break

        for i in range(1, 9):
            try:
                if get_color(board, x - i, y + i) == COLOR['empty']:
                    possible_moves.append([x - i, y + i])
                elif get_color(board, x - i, y + i) == COLOR['white']:
                    possible_moves.append([x - i, y + i])
                    break
                else:
                    break
            except Exception:
                break

    return possible_moves


def get_moves_knight(board: list, x: int, y: int):
    possible_moves = []
    color = get_color(board, x, y)

    # Проверка для белых фигур
    if color == COLOR['white']:

        if x + 2 <= 8 and y + 1 <= 8 and get_color(board, x + 2, y + 1) != COLOR['white']:
            possible_moves.append([x + 2, y + 1])

        if x + 2 <= 8 and y - 1 >= 1 and get_color(board, x + 2, y - 1) != COLOR['white']:
            possible_moves.append([x + 2, y - 1])

        if x - 2 >= 1 and y + 1 <= 8 and get_color(board, x - 2, y + 1) != COLOR['white']:
            possible_moves.append([x - 2, y + 1])

        if x - 2 >= 1 and y - 1 >= 1 and get_color(board, x - 2, y - 1) != COLOR['white']:
            possible_moves.append([x - 2, y - 1])

        if x + 1 <= 8 and y + 2 <= 8 and get_color(board, x + 1, y + 2) != COLOR['white']:
            possible_moves.append([x + 1, y + 2])

        if x + 1 <= 8 and y - 2 >= 1 and get_color(board, x + 1, y - 2) != COLOR['white']:
            possible_moves.append([x + 1, y - 2])

        if x - 1 >= 1 and y + 2 <= 8 and get_color(board, x - 1, y + 2) != COLOR['white']:
            possible_moves.append([x - 1, y + 2])

        if x - 1 >= 1 and y - 2 >= 1 and get_color(board, x - 1, y - 2) != COLOR['white']:
            possible_moves.append([x - 1, y - 2])

    # Проверка для чёрных фигур
    if color == COLOR['black']:

        if x + 2 <= 8 and y + 1 <= 8 and get_color(board, x + 2, y + 1) != COLOR['black']:
            possible_moves.append([x + 2, y + 1])

        if x + 2 <= 8 and y - 1 >= 1 and get_color(board, x + 2, y - 1) != COLOR['black']:
            possible_moves.append([x + 2, y - 1])

        if x - 2 >= 1 and y + 1 <= 8 and get_color(board, x - 2, y + 1) != COLOR['black']:
            possible_moves.append([x - 2, y + 1])

        if x - 2 >= 1 and y - 1 >= 1 and get_color(board, x - 2, y - 1) != COLOR['black']:
            possible_moves.append([x - 2, y - 1])

        if x + 1 <= 8 and y + 2 <= 8 and get_color(board, x + 1, y + 2) != COLOR['black']:
            possible_moves.append([x + 1, y + 2])

        if x + 1 <= 8 and y - 2 >= 1 and get_color(board, x + 1, y - 2) != COLOR['black']:
            possible_moves.append([x + 1, y - 2])

        if x - 1 >= 1 and y + 2 <= 8 and get_color(board, x - 1, y + 2) != COLOR['black']:
            possible_moves.append([x - 1, y + 2])

        if x - 1 >= 1 and y - 2 >= 1 and get_color(board, x - 1, y - 2) != COLOR['black']:
            possible_moves.append([x - 1, y - 2])

    return possible_moves


def check_piece(board: list, x: int, y: int):
    if board[x][y].strip().upper() == 'P':
        return get_moves_pawn(board, x, y)

    if board[x][y].strip().upper() == 'K':
        return get_moves_king(board, x, y)

    if board[x][y].strip().upper() == 'Q':
        return get_moves_queen(board, x, y)

    if board[x][y].strip().upper() == 'B':
        return get_moves_bishop(board, x, y)

    if board[x][y].strip().upper() == 'R':
        return get_moves_rook(board, x, y)

    if board[x][y].strip().upper() == 'N':
        return get_moves_knight(board, x, y)


def piece_move(board: list, point_from: list[int], point_to: list[int]) -> None:
    board[point_to[0]][point_to[1]] = board[point_from[0]][point_from[1]]
    board[point_from[0]][point_from[1]] = ' . '


def player_step(board: list, player: int):
    err_msg = ''

    # Определение игрока
    if player == 0:
        print(f"\033[32m{PLAYERS[0]}: \033[39m", end='')
    elif player == 1:
        print(f"\033[33m{PLAYERS[1]}: \033[39m", end='')

    # Пользователь вводит свой ход в виде строки,
    # после чего он сразу преобразуется в список символов

    step = list(input().strip().upper())

    # Для прекращении партии необходимо ввести слово "stop"
    if ''.join(step) == 'STOP':
        return 'STOP'
    elif ''.join(step) == 'ROLLBACK':
        return 'ROLLBACK'

    # Валидация введённых данных
    if len(step) != 5:
        err_msg = 'Ход указан не в верном формате!\nПример прафильного формата: b2-b3\n\nПовторите попытку'
        return [False, err_msg]
    elif step[2] != '-':
        err_msg = 'Между указанными ячейками должно быть тире'
        return [False, err_msg]
    elif step[1] not in map(str, ROW) and step[4] not in map(str, ROW):
        err_msg = 'Вторым символом ячейки должно быть число от 1 до 8'
        return [False, err_msg]
    elif step[0] not in COL or step[3] not in COL:
        err_msg = 'Вторым символом ячейки должна быть буква от A до H'
        return [False, err_msg]

    from_to = [[9 - int(step[1]), COL[step[0]]],
               [9 - int(step[4]), COL[step[3]]]]

    if from_to[1] in check_piece(board, from_to[0][0], from_to[0][1]):
        piece_move(board, from_to[0], from_to[1])
        return ''.join(step)
    else:
        return [False, 'Данная фигара не может так ходить, либо Вы пытаетесь переместить пустую ячейку']


def file_write_history(hist: list[str]) -> bool:
    """
    Запись полной нотации партии в файл

    Маска файла будет относительно текущей даты
    party_res_<DAY>_<MONTH>_<YEAR>__<HOURS>_<MINUTES>

    :return: Возвращает True при успешной записи
    """
    if len(hist) > 0:
        today = datetime.now()
        filename = f'./party_res_{today.day}_{today.month}_{today.year}__{today.hour}_{today.minute}.txt'

        with open(filename, 'w', encoding='utf8') as FILE:
            FILE.write(
                f'    {PLAYERS[START_PLAYER % 2][0]}-1  |  {PLAYERS[(START_PLAYER + 1) % 2][0]}-2\n')
            for line in hist:
                FILE.write(line + '\n')
        return True

    print('Игроки не сделали ни одного хода. Файл не создался')
    return False


# Глобальные переменные
# обозначаем цвета, которые будут использоваться на шахматной доске
COLOR = {
    'empty': 0,  # Обозначаются пустые клетки доски
    'black': 1,  # Обозначаются чёрные фигуры
    'white': 2,  # Обозначаются белые фигуры
}

# Словарь из названий столбцов и их нумерацией
COL = {'A': 1, 'B': 2,
       'C': 3, 'D': 4,
       'E': 5, 'F': 6,
       'G': 7, 'H': 8}

ROW = [1, 2, 3, 4, 5, 6, 7, 8]

# Список для записи ходов
MOVES_HISTORY = []

# Список ходов для отката
MOVES_ROLLBACK = []

# Список с именами игроков
PLAYERS = ['Player #1', 'Player #2']

# Номер игрока, начинающий партию
START_PLAYER = 0

# Ходы сделанные игроками
ALL_MOVES = ''

# Кол-во ходов сделанных игроками
AMOUNT_MOVES = 0

# Список для построения доски
# Изначально фигуры расставлены как в начале партии
DESK = [
    #    A  B  C  D  E  F  G  H
    # 8  r  n  b  q  k  b  n  r  8
    # 7  p  p  p  p  p  p  p  p  7
    # 6  .  .  .  .  .  .  .  .  6
    # 5  .  .  .  .  .  .  .  .  5
    # 4  .  .  .  .  .  .  .  .  4
    # 3  .  .  .  .  .  .  .  .  3
    # 2  P  P  P  P  P  P  P  P  2
    # 1  R  N  B  Q  K  B  N  R  1
    #    A  B  C  D  E  F  G  H

    ['   ', '\x1b[31m A \x1b[39m', '\x1b[31m B \x1b[39m', '\x1b[31m C \x1b[39m', '\x1b[31m D \x1b[39m',
     '\x1b[31m E \x1b[39m', '\x1b[31m F \x1b[39m', '\x1b[31m G \x1b[39m', '\x1b[31m H \x1b[39m', '   '],

    ['\x1b[31m 8 \x1b[39m', ' r ', ' n ', ' b ', ' q ', ' k ', ' b ', ' n ', ' r ', '\x1b[31m 8 \x1b[39m'],

    ['\x1b[31m 7 \x1b[39m', ' p ', ' p ', ' p ', ' p ', ' p ', ' p ', ' p ', ' p ', '\x1b[31m 7 \x1b[39m'],

    ['\x1b[31m 6 \x1b[39m', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', '\x1b[31m 6 \x1b[39m'],

    ['\x1b[31m 5 \x1b[39m', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', '\x1b[31m 5 \x1b[39m'],

    ['\x1b[31m 4 \x1b[39m', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', '\x1b[31m 4 \x1b[39m'],

    ['\x1b[31m 3 \x1b[39m', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', '\x1b[31m 3 \x1b[39m'],

    ['\x1b[31m 2 \x1b[39m', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', '\x1b[31m 2 \x1b[39m'],

    ['\x1b[31m 1 \x1b[39m', ' R ', ' N ', ' B ', ' Q ', ' K ', ' B ', ' N ', ' R ', '\x1b[31m 1 \x1b[39m'],

    ['   ', '\x1b[31m A \x1b[39m', '\x1b[31m B \x1b[39m', '\x1b[31m C \x1b[39m', '\x1b[31m D \x1b[39m',
     '\x1b[31m E \x1b[39m', '\x1b[31m F \x1b[39m', '\x1b[31m G \x1b[39m', '\x1b[31m H \x1b[39m', '   ']
]

if __name__ == '__main__':
    # greeting(PLAYERS, START_PLAYER)

    desk_show(DESK)

    while True:
        step = player_step(DESK, START_PLAYER % 2)

        if step == 'STOP':
            print("\n\nПАРТИЯ ОКОНЧЕНА!\nСпасибо за игру)\n")
            break

        if step == 'ROLLBACK':
            if len(MOVES_ROLLBACK) > 0:

                rollback_step_from = MOVES_ROLLBACK[-1][3:]
                rollback_step_to = MOVES_ROLLBACK[-1][:2]

                MOVES_ROLLBACK.pop()


                piece_move(DESK, [9 - int(rollback_step_from[1]), COL[rollback_step_from[0]]],
                           [9 - int(rollback_step_to[1]), COL[rollback_step_to[0]]])
                print(f'Сделан откат хода из {rollback_step_from} в {rollback_step_to}')
            else:
                print('Ходов ещё не было сделано, ОТКАТ НЕВОЗМОЖЕН!')
                continue

        # Проверка ходов на валидность
        # При возникновении ошибок ход повторяется
        if step[0] == False:
            print("\nОшибка!")
            if step[1] == '':
                print("Данная фигура не может так ходить\n"
                      "Повторите попытку\n")
            else:
                print(step[1] + '\n')
            continue
        else:
            desk_show(DESK)
            ALL_MOVES += step
            if step != 'ROLLBACK':
                MOVES_ROLLBACK.append(step)
            START_PLAYER += 1

        # Добавление ходов в список MOVES_HISTORY
        if len(ALL_MOVES) > 8:
            AMOUNT_MOVES += 1
            MOVES_HISTORY.append(
                f'{AMOUNT_MOVES}. {ALL_MOVES[:5]} | {ALL_MOVES[5:]}')
            ALL_MOVES = ''

    file_write_history(MOVES_HISTORY)
