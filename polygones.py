import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

fig, ax = plt.subplots()

# Размер холста
plt.plot(25, 25)
ax.grid()


def average(*numbers):
    return sum(numbers)/len(numbers)


class Triangle_Cust():
    size = 2
    amount = 1
    step = 1
    color = 'black'

    def __init__(self, size: int, amount: int, step: int, color: str):
        self.size = size
        self.amount = amount
        self.step = step
        self.color = color

    def get_figure(self) -> None:
        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):

            dots = np.array([[1+distance, 1],
                             [average(1, self.size) + distance, self.size],
                             [self.size + distance, 1],
                             [1 + distance, 1]])

            ax.add_patch(Polygon(dots,
                                 edgecolor=self.color,
                                 facecolor=self.color))

            distance += self.size + self.step

    def rotate(self, xy, deg, rp):
        xy = xy-rp
        i = 0
        while i < len(xy):
            xy[i][0] = xy[i][0] * \
                np.cos(np.deg2rad(deg))-(xy[i][1]*np.sin(np.deg2rad(deg)))
            xy[i][1] = xy[i][0] * \
                np.sin(np.deg2rad(deg))+xy[i][1]*np.cos(np.deg2rad(deg))
            i += 1
        return xy+rp

    def tr_rotate(self, degrees: int):
        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):
            x = 1

            dots = np.array([[1+distance, 1],
                             [average(1, self.size) + distance, self.size],
                             [self.size + distance, 1],
                             [1 + distance, 1]])

            triang = Polygon(dots,
                             edgecolor=self.color,
                             facecolor=self.color)

            # print(triang.get_xy(), -40, triang.get_xy()
            #       [0], end='\n\n\n', sep='|||')

            triang.set_xy(self.rotate(
                triang.get_xy(), -40, triang.get_xy()[0]))
            ax.add_patch(triang)

            distance += self.size + self.step

    def tr_translate(self, x: int, y: int):
        for _ in range(self.amount):
            ax.patches.pop()

        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):

            dots = np.array([[1+distance+x, 1+y],
                             [average(1, self.size) + distance+x, self.size+y],
                             [self.size + distance+x, 1+y],
                             [1 + distance+x, 1+y]])

            ax.add_patch(Polygon(dots,
                                 edgecolor=self.color,
                                 facecolor=self.color))

            distance += self.size + self.step

    def tr_symmetry(self, y: int):
        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):

            dots = np.array([[1+distance, self.size+y],
                             [average(1, self.size) + distance, 1+y],
                             [self.size + distance, self.size+y],
                             [1 + distance, self.size+y]])

            ax.add_patch(Polygon(dots,
                                 edgecolor=self.color,
                                 facecolor=self.color))

            distance += self.size + self.step


class Polygon_Cust():
    color = 'red'
    dots = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])

    def __init__(self, color: str, *dots):
        self.color = color
        self.dots = np.array(dots)

    def get_figure(self) -> None:
        self.dots = np.array(list(self.dots))
        ax.add_patch(
            Polygon(self.dots, edgecolor=self.color, facecolor=self.color))


class Rectangle_Cust():
    def get_figure(width: int, height: int, amount=1, step=5) -> None:

        amount = 1 if amount <= 0 else amount
        step = 1 if step <= 0 else step

        distance = 0

        for _ in range(1, amount+1):
            rect = Rectangle((distance, 1), width, height, linewidth=1,
                             edgecolor='red', facecolor='red')

            ax.add_patch(rect)

            distance += width + step


class Hexagon_Cust():
    def get_figure(size: int, amount: int, step: int):
        distance = 0

        size = 2 if size <= 1 else size

        for _ in range(amount):
            dots = np.array([[1 + distance, 0],
                            [0 + distance, 1],
                            [0 + distance, 2],
                            [1 + distance, 3],
                            [2 + distance, 3],
                            [3 + distance, 2],
                            [3 + distance, 1],
                            [2 + distance, 0],
                            [1 + distance, 0]])
            ax.add_patch(Polygon(dots, edgecolor='gray', facecolor='gray'))
            distance += size*2+step


# sequence = Polygon_Cust('red', [0, 0], [0, 1], [1, 1], [2, 2], [1, 0], [0, 0])
sequence = Triangle_Cust(2, 5, 1, 'red')
# sequence = Rectangle_Cust()
# sequence = Hexagon_Cust()

# sequence.get_figure()
# sequence.tr_translate(5, 5)
sequence.tr_symmetry(-5)
# sequence.tr_rotate(5)

# ax.add_patch(Polygon(np.array([[average(1, 2), 0],
#                                [0, 2], [3, 2], [average(1, 2), 0]])))

plt.show()
