"""
Шахматы
"""

import art
from random import randint
from time import sleep
from datetime import datetime

# Обозначаем цвета, которые будут использоваться на шахматной доске
COLOR = {
    'empty': 0,  # Обозначаются пустые клетки доски
    'black': 1,
    'white': 2
}

# Словарь из названий слобцов и их нумерацией
COL = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
       'E': 5, 'F': 6, 'G': 7, 'H': 8}

ROW = [1, 2, 3, 4, 5, 6, 7, 8]

# Список для записи ходов
MOVES_HISTORY = []


class Empty:
    err_msg = ''
    """
    Класс создан для обозначения пустых полей на доске

    Если вывести данный объект, то он будет представлен в виде " . "
    """

    def __init__(self):
        self.color = COLOR['empty']

    def __str__(self):
        return ' . '

    def get_color(self):
        return self.color

    def get_moves(self, board, x: int, y: int) -> list:
        return []


class Piece:
    """
    Общий класс для всех фигур

    В нём указаны основные свойства всех фигур
    """
    # Массив и строковых значений фигуры
    value = []

    def __init__(self, color):
        self.color = color

    def __str__(self):
        """
        Выводит данной объект в виде строки, значение берётся из переменной value
        """
        if self.color == COLOR['white']:
            return self.value[0]
        return self.value[1]

    def get_color(self, x: int, y: int) -> int:
        """
        Возвращает цвет фигуры, находящаяся на указанных координатах
        """
        return self.board[x][y].color

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []
        return possible_moves


class Pawn(Piece):
    """
    Описание фигуры "Пешка"
    """
    value = [' P ', ' p ']

    def get_moves(self, board, x: int, y: int) -> list:
        """
        Принимает на вход координаты фигуры и возвращает список из координат,
        по которым может передвигаться фигура

        :return: Список координат возможных ходов фигуры
        """
        possible_moves = []

        # Проверка для чёрных фигур
        if self.color == COLOR['black'] \
                and x == 2 \
                and board.get_color(x + 1, y) == COLOR['empty'] \
                and board.get_color(x + 2, y) == COLOR['empty']:
            possible_moves.append([x + 1, y])
            possible_moves.append([x + 2, y])
        elif self.color == COLOR['black'] \
                and x >= 2 \
                and board.get_color(x + 1, y) == COLOR['empty']:
            possible_moves.append([x + 1, y])

        # Проверка для белых фигур
        if self.color == COLOR['white'] \
                and x == 7 \
                and board.get_color(x - 1, y) == COLOR['empty'] \
                and board.get_color(x - 2, y) == COLOR['empty']:
            possible_moves.append([x - 1, y])
            possible_moves.append([x - 2, y])
        elif self.color == COLOR['white'] \
                and x <= 7 \
                and board.get_color(x - 1, y) == COLOR['empty']:
            possible_moves.append([x - 1, y])

        return possible_moves


class King(Piece):
    """
    Описание фигуры "Король"
    """
    value = [' K ', ' k ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        # Проверка для белых фигур
        if self.color == COLOR['white']:

            if board.get_color(x - 1, y) != COLOR['white']:
                possible_moves.append([x - 1, y])

            if board.get_color(x + 1, y) != COLOR['white']:
                possible_moves.append([x + 1, y])

            if board.get_color(x - 1, y - 1) != COLOR['white']:
                possible_moves.append([x - 1, y - 1])

            if board.get_color(x - 1, y + 1) != COLOR['white']:
                possible_moves.append([x - 1, y + 1])

            if board.get_color(x + 1, y - 1) != COLOR['white']:
                possible_moves.append([x + 1, y - 1])

            if board.get_color(x + 1, y + 1) != COLOR['white']:
                possible_moves.append([x + 1, y + 1])

            if board.get_color(x, y - 1) != COLOR['white']:
                possible_moves.append([x, y - 1])

            if board.get_color(x, y + 1) != COLOR['white']:
                possible_moves.append([x, y + 1])

        # Проверка для чёрных фигур
        if self.color == COLOR['black']:

            if board.get_color(x - 1, y) != COLOR['black']:
                possible_moves.append([x - 1, y])

            if board.get_color(x + 1, y) != COLOR['black']:
                possible_moves.append([x + 1, y])

            if board.get_color(x - 1, y - 1) != COLOR['black']:
                possible_moves.append([x - 1, y - 1])

            if board.get_color(x - 1, y + 1) != COLOR['black']:
                possible_moves.append([x - 1, y + 1])

            if board.get_color(x + 1, y - 1) != COLOR['black']:
                possible_moves.append([x + 1, y - 1])

            if board.get_color(x + 1, y + 1) != COLOR['black']:
                possible_moves.append([x + 1, y + 1])

            if board.get_color(x, y - 1) != COLOR['black']:
                possible_moves.append([x, y - 1])

            if board.get_color(x, y + 1) != COLOR['black']:
                possible_moves.append([x, y + 1])

        return possible_moves


class Queen(Piece):
    """
    Описание фигуры "Ферзь"
    """
    value = [' Q ', ' q ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        # Проверка для белых фигур по вертикали/горизонтали
        if self.color == COLOR['white']:

            for i in range(1, 9 - x):
                if board.get_color(x + i, y) == COLOR['empty']:
                    possible_moves.append([x + i, y])
                elif board.get_color(x + i, y) == COLOR['black']:
                    possible_moves.append([x + i, y])
                    break
                elif board.get_color(x + i, y) == COLOR['white']:
                    break

            for i in range(1, x):
                if board.get_color(x - i, y) == COLOR['empty']:
                    possible_moves.append([x - i, y])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x - i, y])
                    break
                elif board.get_color(x - i, y) == COLOR['white']:
                    break

            for i in range(1, 9 - y):
                if board.get_color(x, y + i) == COLOR['empty']:
                    possible_moves.append([x, y + i])
                elif board.get_color(x, y + i) == COLOR['black']:
                    possible_moves.append([x, y + i])
                    break
                elif board.get_color(x, y + i) == COLOR['white']:
                    break

            for i in range(1, y):
                if board.get_color(x, y - i) == COLOR['empty']:
                    possible_moves.append([x, y - i])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x, y - i])
                    break
                elif board.get_color(x, y - i) == COLOR['white']:
                    break

            # Проверка для белых фигур по диагоналям
            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y + i) == COLOR['empty']:
                        possible_moves.append([x + i, y + i])
                    elif board.get_color(x + i, y + i) == COLOR['black']:
                        possible_moves.append([x + i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y - i) == COLOR['empty']:
                        possible_moves.append([x + i, y - i])
                    elif board.get_color(x + i, y - i) == COLOR['black']:
                        possible_moves.append([x + i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y - i) == COLOR['empty']:
                        possible_moves.append([x - i, y - i])
                    elif board.get_color(x - i, y - i) == COLOR['black']:
                        possible_moves.append([x - i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y + i) == COLOR['empty']:
                        possible_moves.append([x - i, y + i])
                    elif board.get_color(x - i, y + i) == COLOR['black']:
                        possible_moves.append([x - i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

        # Проверка для чёрных фигур по вертикали/горизонтали
        if self.color == COLOR['black']:

            for i in range(1, 9 - x):
                if board.get_color(x + i, y) == COLOR['empty']:
                    possible_moves.append([x + i, y])
                elif board.get_color(x + i, y) == COLOR['black']:
                    possible_moves.append([x + i, y])
                    break
                elif board.get_color(x + i, y) == COLOR['white']:
                    break

            for i in range(1, x):
                if board.get_color(x - i, y) == COLOR['empty']:
                    possible_moves.append([x - i, y])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x - i, y])
                    break
                elif board.get_color(x - i, y) == COLOR['white']:
                    break

            for i in range(1, 9 - y):
                if board.get_color(x, y + i) == COLOR['empty']:
                    possible_moves.append([x, y + i])
                elif board.get_color(x, y + i) == COLOR['black']:
                    possible_moves.append([x, y + i])
                    break
                elif board.get_color(x, y + i) == COLOR['white']:
                    break

            for i in range(1, y):
                if board.get_color(x, y - i) == COLOR['empty']:
                    possible_moves.append([x, y - i])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x, y - i])
                    break
                elif board.get_color(x, y - i) == COLOR['white']:
                    break

            # Проверка для чёрных фигур по диагоналям
            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y + i) == COLOR['empty']:
                        possible_moves.append([x + i, y + i])
                    elif board.get_color(x + i, y + i) == COLOR['white']:
                        possible_moves.append([x + i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y - i) == COLOR['empty']:
                        possible_moves.append([x + i, y - i])
                    elif board.get_color(x + i, y - i) == COLOR['white']:
                        possible_moves.append([x + i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y - i) == COLOR['empty']:
                        possible_moves.append([x - i, y - i])
                    elif board.get_color(x - i, y - i) == COLOR['white']:
                        possible_moves.append([x - i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y + i) == COLOR['empty']:
                        possible_moves.append([x - i, y + i])
                    elif board.get_color(x - i, y + i) == COLOR['white']:
                        possible_moves.append([x - i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

        return possible_moves


class Rook(Piece):
    """
    Описание фигуры "Ладья"
    """
    value = [' R ', ' r ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        # Проверка для белых фигур
        if self.color == COLOR['white']:

            for i in range(1, 9 - x):
                if board.get_color(x + i, y) == COLOR['empty']:
                    possible_moves.append([x + i, y])
                elif board.get_color(x + i, y) == COLOR['black']:
                    possible_moves.append([x + i, y])
                    break
                elif board.get_color(x + i, y) == COLOR['white']:
                    break

            for i in range(1, x):
                if board.get_color(x - i, y) == COLOR['empty']:
                    possible_moves.append([x - i, y])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x - i, y])
                    break
                elif board.get_color(x - i, y) == COLOR['white']:
                    break

            for i in range(1, 9 - y):
                if board.get_color(x, y + i) == COLOR['empty']:
                    possible_moves.append([x, y + i])
                elif board.get_color(x, y + i) == COLOR['black']:
                    possible_moves.append([x, y + i])
                    break
                elif board.get_color(x, y + i) == COLOR['white']:
                    break

            for i in range(1, y):
                if board.get_color(x, y - i) == COLOR['empty']:
                    possible_moves.append([x, y - i])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x, y - i])
                    break
                elif board.get_color(x, y - i) == COLOR['white']:
                    break

        # Проверка для чёрных фигур
        if self.color == COLOR['black']:

            for i in range(1, 9 - x):
                if board.get_color(x + i, y) == COLOR['empty']:
                    possible_moves.append([x + i, y])
                elif board.get_color(x + i, y) == COLOR['black']:
                    possible_moves.append([x + i, y])
                    break
                elif board.get_color(x + i, y) == COLOR['white']:
                    break

            for i in range(1, x):
                if board.get_color(x - i, y) == COLOR['empty']:
                    possible_moves.append([x - i, y])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x - i, y])
                    break
                elif board.get_color(x - i, y) == COLOR['white']:
                    break

            for i in range(1, 9 - y):
                if board.get_color(x, y + i) == COLOR['empty']:
                    possible_moves.append([x, y + i])
                elif board.get_color(x, y + i) == COLOR['black']:
                    possible_moves.append([x, y + i])
                    break
                elif board.get_color(x, y + i) == COLOR['white']:
                    break

            for i in range(1, y):
                if board.get_color(x, y - i) == COLOR['empty']:
                    possible_moves.append([x, y - i])
                elif board.get_color(x - i, y) == COLOR['black']:
                    possible_moves.append([x, y - i])
                    break
                elif board.get_color(x, y - i) == COLOR['white']:
                    break

        return possible_moves


class Bishop(Piece):
    """
    Описание фигуры "Слон"
    """
    value = [' B ', ' b ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        if self.color == COLOR['white']:

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y + i) == COLOR['empty']:
                        possible_moves.append([x + i, y + i])
                    elif board.get_color(x + i, y + i) == COLOR['black']:
                        possible_moves.append([x + i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y - i) == COLOR['empty']:
                        possible_moves.append([x + i, y - i])
                    elif board.get_color(x + i, y - i) == COLOR['black']:
                        possible_moves.append([x + i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y - i) == COLOR['empty']:
                        possible_moves.append([x - i, y - i])
                    elif board.get_color(x - i, y - i) == COLOR['black']:
                        possible_moves.append([x - i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y + i) == COLOR['empty']:
                        possible_moves.append([x - i, y + i])
                    elif board.get_color(x - i, y + i) == COLOR['black']:
                        possible_moves.append([x - i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

        if self.color == COLOR['black']:

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y + i) == COLOR['empty']:
                        possible_moves.append([x + i, y + i])
                    elif board.get_color(x + i, y + i) == COLOR['white']:
                        possible_moves.append([x + i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x + i, y - i) == COLOR['empty']:
                        possible_moves.append([x + i, y - i])
                    elif board.get_color(x + i, y - i) == COLOR['white']:
                        possible_moves.append([x + i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y - i) == COLOR['empty']:
                        possible_moves.append([x - i, y - i])
                    elif board.get_color(x - i, y - i) == COLOR['white']:
                        possible_moves.append([x - i, y - i])
                        break
                    else:
                        break
                except Exception:
                    break

            for i in range(1, 9):
                try:
                    if board.get_color(x - i, y + i) == COLOR['empty']:
                        possible_moves.append([x - i, y + i])
                    elif board.get_color(x - i, y + i) == COLOR['white']:
                        possible_moves.append([x - i, y + i])
                        break
                    else:
                        break
                except Exception:
                    break

        return possible_moves


class Knight(Piece):
    """
    Описание фигуры "Конь"
    """
    value = [' N ', ' n ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        # Проверка для белых фигур
        if self.color == COLOR['white']:

            if x + 2 <= 8 and y + 1 <= 8 and board.get_color(x + 2, y + 1) != COLOR['white']:
                possible_moves.append([x + 2, y + 1])

            if x + 2 <= 8 and y - 1 >= 1 and board.get_color(x + 2, y - 1) != COLOR['white']:
                possible_moves.append([x + 2, y - 1])

            if x - 2 >= 1 and y + 1 <= 8 and board.get_color(x - 2, y + 1) != COLOR['white']:
                possible_moves.append([x - 2, y + 1])

            if x - 2 >= 1 and y - 1 >= 1 and board.get_color(x - 2, y - 1) != COLOR['white']:
                possible_moves.append([x - 2, y - 1])

            if x + 1 <= 8 and y + 2 <= 8 and board.get_color(x + 1, y + 2) != COLOR['white']:
                possible_moves.append([x + 1, y + 2])

            if x + 1 <= 8 and y - 2 >= 1 and board.get_color(x + 1, y - 2) != COLOR['white']:
                possible_moves.append([x + 1, y - 2])

            if x - 1 >= 1 and y + 2 <= 8 and board.get_color(x - 1, y + 2) != COLOR['white']:
                possible_moves.append([x - 1, y + 2])

            if x - 1 >= 1 and y - 2 >= 1 and board.get_color(x - 1, y - 2) != COLOR['white']:
                possible_moves.append([x - 1, y - 2])

        # Проверка для чёрных фигур
        if self.color == COLOR['black']:

            if x + 2 <= 8 and y + 1 <= 8 and board.get_color(x + 2, y + 1) != COLOR['black']:
                possible_moves.append([x + 2, y + 1])

            if x + 2 <= 8 and y - 1 >= 1 and board.get_color(x + 2, y - 1) != COLOR['black']:
                possible_moves.append([x + 2, y - 1])

            if x - 2 >= 1 and y + 1 <= 8 and board.get_color(x - 2, y + 1) != COLOR['black']:
                possible_moves.append([x - 2, y + 1])

            if x - 2 >= 1 and y - 1 >= 1 and board.get_color(x - 2, y - 1) != COLOR['black']:
                possible_moves.append([x - 2, y - 1])

            if x + 1 <= 8 and y + 2 <= 8 and board.get_color(x + 1, y + 2) != COLOR['black']:
                possible_moves.append([x + 1, y + 2])

            if x + 1 <= 8 and y - 2 >= 1 and board.get_color(x + 1, y - 2) != COLOR['black']:
                possible_moves.append([x + 1, y - 2])

            if x - 1 >= 1 and y + 2 <= 8 and board.get_color(x - 1, y + 2) != COLOR['black']:
                possible_moves.append([x - 1, y + 2])

            if x - 1 >= 1 and y - 2 >= 1 and board.get_color(x - 1, y - 2) != COLOR['black']:
                possible_moves.append([x - 1, y - 2])

        return possible_moves


class Desk:
    """
    Класс представляет собой шахматную доску

    Создаёт массив объектов (фигур)
    При выводит на экран, возвращает строковое представление данного массива
    """

    def __init__(self):
        """
        Инициализируем доску 8х8 с нумерацией и обозначением полей
        """

        letter = ['   ', ' A ', ' B ', ' C ', ' D ',
                  ' E ', ' F ', ' G ', ' H ', '   ']
        num_ord = ['   ', ' 8 ', ' 7 ', ' 6 ',
                   ' 5 ', ' 4 ', ' 3 ', ' 2 ', ' 1 ', '   ']

        self.board = [[Empty() for _ in range(10)] for _ in range(10)]

        for i in range(10):
            # Выводим вертикали и горизонтали
            self.board[0][i] = '\033[31m' + letter[i] + '\033[39m'
            self.board[-1][i] = '\033[31m' + letter[i] + '\033[39m'
            self.board[i][0] = '\033[31m' + num_ord[i] + '\033[39m'
            self.board[i][-1] = '\033[31m' + num_ord[i] + '\033[39m'

            # Раскладываем фигуры на доске

            # Пешка
            if 0 < i < 9:
                self.board[2][i] = Pawn(COLOR['black'])
                self.board[7][i] = Pawn(COLOR['white'])

            # Король
            self.board[1][5] = King(COLOR['black'])
            self.board[8][5] = King(COLOR['white'])

            # Ферзь
            self.board[1][4] = Queen(COLOR['black'])
            self.board[8][4] = Queen(COLOR['white'])

            # Слон
            self.board[1][3] = Bishop(COLOR['black'])
            self.board[8][3] = Bishop(COLOR['white'])
            self.board[1][6] = Bishop(COLOR['black'])
            self.board[8][6] = Bishop(COLOR['white'])

            # Конь
            self.board[1][2] = Knight(COLOR['black'])
            self.board[8][2] = Knight(COLOR['white'])
            self.board[1][7] = Knight(COLOR['black'])
            self.board[8][7] = Knight(COLOR['white'])

            # Ладья
            self.board[1][1] = Rook(COLOR['black'])
            self.board[8][1] = Rook(COLOR['white'])
            self.board[1][8] = Rook(COLOR['black'])
            self.board[8][8] = Rook(COLOR['white'])

    def __str__(self):
        """
        Возвращает строковое представление шахматной доски с актуальным расположением фигур

        :return: Шахматная доска в виде строки
        """
        result = str()
        for i in range(10):
            result += ''.join(map(str, self.board[i])) + '\n'

        return f'\n- - - - - - - - - - - - - - - - - \n\n' + result

    def get_color(self, x, y):
        """
        Обращается к объекту по указанным координатам и возвращает его цвет
        """
        return self.board[x][y].color

    def get_moves(self, x, y):
        """
        Обращается к объекту по указанным координатам и возвращает список
        возможных ходов данной фигуры
        """
        return self.board[x][y].get_moves(self, x, y)

    def move(self, point_from: list[int], point_to: list[int]):
        """
        Передвигает фигуру по указанным координатам
        """
        self.board[point_to[0]][point_to[1]] = self.board[point_from[0]][point_from[1]]
        self.board[point_from[0]][point_from[1]] = Empty()


class Game:
    """
    Является сборным классом
    Необходим для осуществления геймплея и запуска методов других классов
    """
    steps = 0
    players = ['', '']
    desk = None
    start_player = 0

    def __init__(self):
        """
        При инициализации данного объекта происходит приветсвие
        После необходим ввод имён двух игроков
        """
        print('\033[34m')
        art.tprint('CHESS')

        print("Добро пожаловать в наш небольшой шахматный мир!\n"
              "Пожалуйста, представьтесь")

        print('\033[32m')
        self.players[0] = input('Игрок 1: ')

        print('\033[33m')
        self.players[1] = input('Игрок 2: ')
        print('\033[39m')

        print("ОТЛИЧНО!\n"
              "Теперь 'подбросим монетку' для определения того,\n"
              "кто будеи играть за белые фигуры", end='')

        for _ in range(3):
            sleep(1)
            print(' . ', end='')

        # Проходит жеребьёвка, после которой определяется игрок начинающий партию
        num = randint(0, 2)
        print('\n')
        sleep(1)
        if num == 1:
            print(f'Партию начинает - \033[32m{self.players[0]}\n\033[39m')
        else:
            self.start_player = 1
            print(f'Партию начинает - \033[33m{self.players[1]}\n\033[39m')

        sleep(2)
        art.tprint("Let's      start!")
        sleep(1)

        self.desk = Desk()
        self.desk_upload()

    def player_step(self, player: int):
        """
        Данный метод осущетсвляет ход игрока на шахматной доске
        """

        err_msg = ''

        # Определение игрока
        if player == 0:
            print(f"\033[32m{self.players[0]}: \033[39m", end='')
        elif player == 1:
            print(f"\033[33m{self.players[1]}: \033[39m", end='')

        # Пользователь вводит свой ход в виде строки,
        # после чего он сразу преобразуется в список символов

        step = list(input().strip().upper())

        # Для прекращении партии необходимо ввести слово "stop"
        if ''.join(step) == 'STOP':
            return 'STOP'

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

        if from_to[1] in self.desk.get_moves(from_to[0][0], from_to[0][1]):
            self.desk.move(from_to[0], from_to[1])
            return ''.join(step)
        else:
            return [False, 'Данная фигара не может так ходить, либо Вы пытаетесь переместить пустую ячейку']

    def desk_upload(self):
        print(self.desk)


if __name__ == '__main__':
    game = Game()
    all_moves = ''
    amount_moves = 0
    player = game.start_player

    while True:

        step = game.player_step(player % 2)

        if step == 'STOP':
            print("\n\nПАРТИЯ ОКОНЧЕНА!\nСпасибо за игру)\n")
            break

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
            game.desk_upload()
            all_moves += step
            player += 1

        # Добавление ходов в список MOVES_HISTORY
        if len(all_moves) > 8:
            amount_moves += 1
            MOVES_HISTORY.append(
                f'{amount_moves}. {all_moves[:5]} | {all_moves[5:]}')
            all_moves = ''

    # Запись ходов в файл из списка MOVES_HISTORY
    # Масква файла: party_res_<DAY>_<MONTH>_<YEAR>__<HOURS>_<MINUTES>
    if len(MOVES_HISTORY) > 0:
        today = datetime.now()
        filename = f'party_res_{today.day}_{today.month}_{today.year}__{today.hour}_{today.minute}.txt'

        with open(filename, 'w', encoding='utf8') as FILE:
            FILE.write(
                f'    {game.players[game.start_player % 2][0]}-1  |  {game.players[(game.start_player + 1) % 2][0]}-2\n')
            for line in MOVES_HISTORY:
                FILE.write(line + '\n')

        print(f"Отчёт о Вашей партии записан в файл: {filename}\n\n")
