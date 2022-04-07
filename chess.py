
class Piece():
    value = []

    def __init__(self, color):
        self.color = color
        pass

    def __repr__(self):
        if self.color == 0:
            return self.value[0]
        return self.value[1]


class Pawn(Piece):
    value = [' P ', ' p ']


class King(Piece):
    value = [' K ', ' k ']


class Queen(Piece):
    value = [' Q ', ' q ']


class Rook(Piece):
    value = [' R ', ' r ']


class Bishop(Piece):
    value = [' B ', ' B ']


class Knight (Piece):
    value = [' N ', ' n ']


class Chess_Board():
    """
    Класс Chess_Board - построение доски и вывод на экран
    """

    def __init__(self):
        """
        Инициализируем доску 8х8 с нумерацией и обозначением полей
        """

        words = ['   ', ' A ', ' B ', ' C ', ' D ',
                 ' E ', ' F ', ' G ', ' H ', '   ']
        num_ord = ['   ', ' 8 ', ' 7 ', ' 6 ',
                   ' 5 ', ' 4 ', ' 3 ', ' 2 ', ' 1 ', '   ']

        self.board = [[' . ' for _ in range(10)] for _ in range(10)]

        for i in range(10):
            # Выводим вертикали и горизонтали
            self.board[0][i] = words[i]
            self.board[-1][i] = words[i]
            self.board[i][0] = num_ord[i]
            self.board[i][-1] = num_ord[i]

            # Раскладываем фигуры на доске

            # Пешка
            if 0 < i < 10:
                self.board[2][i] = str(Pawn(1))
                self.board[7][i] = str(Pawn(0))

            # Король
            self.board[1][5] = str(King(1))
            self.board[8][5] = str(King(0))

            # Ферзь
            self.board[1][4] = str(Queen(1))
            self.board[8][4] = str(Queen(0))

            # Слон
            self.board[1][3] = str(Bishop(1))
            self.board[8][3] = str(Bishop(0))
            self.board[1][6] = str(Bishop(1))
            self.board[8][6] = str(Bishop(0))

            # Конь
            self.board[1][2] = str(Knight(1))
            self.board[8][2] = str(Knight(0))
            self.board[1][7] = str(Knight(1))
            self.board[8][7] = str(Knight(0))

            # Ладья
            self.board[1][1] = str(Rook(1))
            self.board[8][1] = str(Rook(0))
            self.board[1][8] = str(Rook(1))
            self.board[8][8] = str(Rook(0))

    def __repr__(self):
        result = str()
        for i in range(10):
            result += ''.join(self.board[i]) + '\n'
        return result


print(Chess_Board())
