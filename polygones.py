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

            dots = np.array([[1 + distance, 1 + distance],
                             [average(1, self.size) + distance,
                              self.size + distance],
                             [self.size + distance, 1 + distance],
                             [1 + distance, 1 + distance]])

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

            dots = np.array([[1 + distance, 1 + distance],
                             [average(1, self.size) + distance,
                              self.size + distance],
                             [self.size + distance, 1 + distance],
                             [1 + distance, 1 + distance]])

            triang = Polygon(dots,
                             edgecolor=self.color,
                             facecolor=self.color)

            triang.set_xy(
                self.rotate(
                    triang.get_xy(),
                    degrees,
                    triang.get_xy()[0])
            )

            ax.add_patch(triang)

            distance += self.size + self.step

    def tr_translate(self, x: int, y: int):

        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):

            dots = np.array([[1 + distance + x, 1 + y + distance],
                             [average(1, self.size) + distance +
                              x, self.size + y + distance],
                             [self.size + distance + x, 1 + y + distance],
                             [1 + distance + x, 1 + y + distance]])

            ax.add_patch(Polygon(dots,
                                 edgecolor=self.color,
                                 facecolor=self.color))

            distance += self.size + self.step

    def tr_symmetry(self, y: int):
        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):

            dots = np.array([[1 + distance, self.size + y + distance],
                             [average(1, self.size) + distance,
                              1 + y + distance],
                             [self.size + distance, self.size + y + distance],
                             [1 + distance, self.size + y + distance]])

            ax.add_patch(Polygon(dots,
                                 edgecolor=self.color,
                                 facecolor=self.color))

            distance += self.size + self.step


class Polygon_Cust():

    def __init__(self, color: str, *dots):
        self.color = color
        self.dots = np.array(dots)

    def get_figure(self) -> None:
        self.dots = np.array(list(self.dots))
        ax.add_patch(
            Polygon(self.dots, edgecolor=self.color, facecolor=self.color))


class Rectangle_Cust():

    def __init__(self, width: int, height: int, amount=1, step=5, color='red'):
        self.width = width
        self.height = height
        self.amount = amount
        self.step = step
        self.color = color

    def get_figure(self) -> None:

        self.amount = 1 if self.amount <= 0 else self.amount
        self.step = 1 if self.step <= 0 else self.step

        distance_width = 0
        distance_height = 0

        for _ in range(self.amount):
            rect = Rectangle((distance_width, distance_height), self.width, self.height,
                             edgecolor=self.color, facecolor=self.color)

            ax.add_patch(rect)

            distance_width += self.width + self.step
            distance_height += self.height + self.step


class Hexagon_Cust():

    def __init__(self, size: int, amount: int, step: int, color: str):
        self.size = size
        self.amount = amount
        self.step = step
        self.color = color

    def get_figure(self):
        distance = 0

        self.size = 2 if self.size <= 1 else self.size

        for _ in range(self.amount):
            dots = np.array([[1 + distance, 0 + distance],
                            [0 + distance, 1 + distance],
                            [0 + distance, 2 + distance],
                            [1 + distance, 3 + distance],
                            [2 + distance, 3 + distance],
                            [3 + distance, 2 + distance],
                            [3 + distance, 1 + distance],
                            [2 + distance, 0 + distance],
                            [1 + distance, 0 + distance]])
            ax.add_patch(
                Polygon(dots, edgecolor=self.color, facecolor=self.color))
            distance += self.size*2+self.step


def iter(size, amount, step):
    figures = [
        Polygon_Cust('black', [0, 0], [0, 1], [1, 1], [2, 2], [1, 0], [0, 0]),
        Rectangle_Cust(size, size, amount, step, 'red'),
        Triangle_Cust(size, amount, step, 'green'),
        Hexagon_Cust(size, amount, step, 'yellow')
    ]

    for figure in figures:
        figure.get_figure()


# figures = Polygon_Cust('yellow', [0, 0], [0, 1], [1, 1], [2, 2], [1, 0], [0, 0])
figures = Triangle_Cust(5, 3, 2, 'pink')
# figures = Rectangle_Cust(5, 10, 3, 2, 'black')
# figures = Hexagon_Cust(2, 10, 1, 'purple')

# figures.get_figure()
# figures.tr_translate(7, -14)
# figures.tr_symmetry(15)
# figures.tr_rotate(30)


# iter(5, 5, 5)
plt.show()
