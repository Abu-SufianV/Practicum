
class Figure():
    value = []

    def __init__(self, color):
        self.color = color
        pass

    def __repr__(self):
        if self.color == 0:
            return self.value[0]
        return self.value[1]


class Pawn(Figure):
    value = [' P ', ' p ']


class Desk():
    """
    Класс Desk - построение доски и вывод на экран
    """

    def __init__(self):
        """
        Инициализируем доску 8х8 с нумерацией и обозначением полей
        """

        words = ['   ', ' A ', ' B ', ' C ', ' D ',
                 ' E ', ' F ', ' G ', ' H ', '   ']
        num_ord = ['   ', ' 8 ', ' 7 ', ' 6 ',
                   ' 5 ', ' 4 ', ' 3 ', ' 2 ', ' 1 ', '   ']

        self.desk = [[' . ' for _ in range(10)] for _ in range(10)]

        for i in range(10):
            self.desk[0][i] = words[i]
            self.desk[-1][i] = words[i]
            self.desk[i][0] = num_ord[i]
            self.desk[i][-1] = num_ord[i]
            if 0 < i < 10:
                self.desk[2][i] = str(Pawn(1))
                self.desk[7][i] = str(Pawn(0))

    def __repr__(self):
        result = str()
        for i in range(10):
            result += ''.join(self.desk[i]) + '\n'
        return result


print(Desk())
