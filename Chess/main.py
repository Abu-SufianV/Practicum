import art
import check_moves
from random import randint
from time import sleep

COLOR = {
    'empty': 0,
    'black': 1,
    'white': 2
}

COL = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
       'E': 5, 'F': 6, 'G': 7, 'H': 8}

ROW = [1, 2, 3, 4, 5, 6, 7, 8]

MOVES_HISTORY = {}


class Empty:

    def __init__(self):
        self.color = COLOR['empty']

    def get_color(self):
        return self.color

    def get_moves(self, board, x: int, y: int) -> list:
        print('ОШИБКА!\n'
              'На данной ячейке нет фигуры\n'
              'Проверьте правильность ввода')
        return []

    def __str__(self):
        return ' . '


class Piece:
    value = []

    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if self.color == COLOR['white']:
            return self.value[0]
        return self.value[1]

    def get_color(self, x: int, y: int) -> int:
        return self.board[x][y].color


class Pawn(Piece):
    value = [' P ', ' p ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

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
        elif self.color == COLOR['white'] \
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
    value = [' K ', ' k ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

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

        elif self.color == COLOR['black']:

            if board.get_color(x - 1, y) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x + 1, y) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x - 1, y - 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x - 1, y + 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x + 1, y - 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x + 1, y + 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x, y - 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

            if board.get_color(x, y + 1) != COLOR['black']:
                possible_moves.append(board.get_color(x - 1, y))

        return possible_moves


class Queen(Piece):
    value = [' Q ', ' q ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

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

        elif self.color == COLOR['black']:

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


class Rook(Piece):
    value = [' R ', ' r ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

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

        elif self.color == COLOR['black']:

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
    value = [' B ', ' b ']

    def get_moves(self, board, x: int, y: int) -> list:
        possible_moves = []

        if self.color == COLOR['white']:

            for i in range(1, 9 - x):
                if board.get_color(x + i, y + i) == COLOR['empty']:
                    possible_moves.append([x + i, y + i])
                elif board.get_color(x + i, y + i) == COLOR['black']:
                    possible_moves.append([x + i, y + i])
                    break
                elif board.get_color(x + i, y + i) == COLOR['white']:
                    break
        #
        #     for i in range(1, x):
        #         if board.get_color(x - i, y) == COLOR['empty']:
        #             possible_moves.append([x - i, y])
        #         elif board.get_color(x - i, y) == COLOR['black']:
        #             possible_moves.append([x - i, y])
        #             break
        #         elif board.get_color(x - i, y) == COLOR['white']:
        #             break
        #
        #     for i in range(1, 9 - y):
        #         if board.get_color(x, y + i) == COLOR['empty']:
        #             possible_moves.append([x, y + i])
        #         elif board.get_color(x, y + i) == COLOR['black']:
        #             possible_moves.append([x, y + i])
        #             break
        #         elif board.get_color(x, y + i) == COLOR['white']:
        #             break
        #
        #     for i in range(1, y):
        #         if board.get_color(x, y - i) == COLOR['empty']:
        #             possible_moves.append([x, y - i])
        #         elif board.get_color(x - i, y) == COLOR['black']:
        #             possible_moves.append([x, y - i])
        #             break
        #         elif board.get_color(x, y - i) == COLOR['white']:
        #             break
        #
        # elif self.color == COLOR['black']:
        #
        #     for i in range(1, 9 - x):
        #         if board.get_color(x + i, y) == COLOR['empty']:
        #             possible_moves.append([x + i, y])
        #         elif board.get_color(x + i, y) == COLOR['black']:
        #             possible_moves.append([x + i, y])
        #             break
        #         elif board.get_color(x + i, y) == COLOR['white']:
        #             break
        #
        #     for i in range(1, x):
        #         if board.get_color(x - i, y) == COLOR['empty']:
        #             possible_moves.append([x - i, y])
        #         elif board.get_color(x - i, y) == COLOR['black']:
        #             possible_moves.append([x - i, y])
        #             break
        #         elif board.get_color(x - i, y) == COLOR['white']:
        #             break
        #
        #     for i in range(1, 9 - y):
        #         if board.get_color(x, y + i) == COLOR['empty']:
        #             possible_moves.append([x, y + i])
        #         elif board.get_color(x, y + i) == COLOR['black']:
        #             possible_moves.append([x, y + i])
        #             break
        #         elif board.get_color(x, y + i) == COLOR['white']:
        #             break
        #
        #     for i in range(1, y):
        #         if board.get_color(x, y - i) == COLOR['empty']:
        #             possible_moves.append([x, y - i])
        #         elif board.get_color(x - i, y) == COLOR['black']:
        #             possible_moves.append([x, y - i])
        #             break
        #         elif board.get_color(x, y - i) == COLOR['white']:
        #             break


class Knight(Piece):
    value = [' N ', ' n ']


class Desk:
    """
    Класс Desk - построение доски и вывод на экран
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
            self.board[0][i] = '\033[31m' + letter[i] + '\033[38m'
            self.board[-1][i] = '\033[31m' + letter[i] + '\033[38m'
            self.board[i][0] = '\033[31m' + num_ord[i] + '\033[38m'
            self.board[i][-1] = '\033[31m' + num_ord[i] + '\033[38m'

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
        При вызове выводит на экран текущее положение фигур на доске

        :return: Шахматная доска в виде строки
        """
        result = str()
        for i in range(10):
            result += ''.join(map(str, self.board[i])) + '\n'

        return f'- - - - - - - - - - - - - - - - - \n\n' + result

    def get_color(self, x, y):
        return self.board[x][y].color

    def get_moves(self, x, y):
        return self.board[x][y].get_moves(self, x, y)

    def move(self, point_from, point_to):
        self.board[point_to[0]][point_to[1]] = self.board[point_from[0]][point_from[1]]
        self.board[point_from[0]][point_from[1]] = Empty()


class TestDesk:

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
            self.board[0][i] = '\033[31m' + letter[i] + '\033[38m'
            self.board[-1][i] = '\033[31m' + letter[i] + '\033[38m'
            self.board[i][0] = '\033[31m' + num_ord[i] + '\033[38m'
            self.board[i][-1] = '\033[31m' + num_ord[i] + '\033[38m'

            self.board[5][5] = Bishop(COLOR['white'])

            self.board[7][7] = King(COLOR['white'])

            self.board[1][1] = Bishop(COLOR['black'])

    def __str__(self):
        """
        При вызове выводит на экран текущее положение фигур на доске

        :return: Шахматная доска в виде строки
        """
        result = str()
        for i in range(10):
            result += ''.join(map(str, self.board[i])) + '\n'

        return f'- - - - - - - - - - - - - - - - - \n\n' + result

    def get_color(self, x, y):
        return self.board[x][y].color

    def get_moves(self, x, y):
        return self.board[x][y].get_moves(self, x, y)

    def move(self, point_from, point_to):
        self.board[point_to[0]][point_to[1]] = self.board[point_from[0]][point_from[1]]
        self.board[point_from[0]][point_from[1]] = Empty()


class Game:
    steps = 0
    player_1 = str()
    player_2 = str()

    def __init__(self):
        print('\033[34m')
        art.tprint('CHESS')

        print("Добро пожаловать в наш небольшой шахматный мир!\n"
              "Пожалуйста, представьтесь")

        print('\033[36m')
        self.player_1 = input('Игрок 1: ')

        print('\033[33m')
        self.player_2 = input('Игрок 2: ')
        print('\033[38m')

        print("ОТЛИЧНО!\n"
              "'Подбросим монетку' для определения того, кто начнёт партию\n")
        sleep(2)

        num = randint(0, 2)
        if num == 1:
            print(f'Партию начинает - {self.player_1}\n')
        else:
            print(f'Партию начинает - {self.player_2}\n')

        # sleep(2)
        # art.tprint('Good   luck!')
        # sleep(1)

        game_desk = Desk()
        print(game_desk)

    def player_step(self, player: str):
        if player == self.player_1:
            print(f"\033[36m{player}:\033[38m", end='')
        elif player == self.player_2:
            print(f"\033[33m{player}:\033[38m", end='')

        step = list(input().strip().upper())
        print(step)
        if len(step) != 5:
            print('Неверно указан ход! Повторите попытку')
        elif step[2] != '-':
            print('Между указанными ячейками должно быть тире')
        elif int(step[1]) not in ROW and int(step[4]) not in ROW:
            print('Вторым символом ячейки должно быть число от 1 до 8')
        elif step[0] not in COL or step[3] not in COL:
            print('Вторым символом ячейки должна быть буква от A до H')
        return (COL[step[0]],int(step[1])), (COL[step[3]],int(step[4]))



# b = TestDesk()
# print(b)
#
# print(len(b.get_moves(5, 5)))
# print(b)

if __name__ == '__main__':
    pass
    game = Game()
    step_from, step_to = game.player_step(game.player_1)
    print(step_from, step_to)