import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Rectangle

fig, ax = plt.subplots()

# Размер холста
plt.plot(25, 25)


def average(x, y):
    return (x+y)/2


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
            dots = np.array([[1+distance, 1], [average(1, self.size) +
                            distance, self.size], [self.size+distance, 1], [1+distance, 1]])
            ax.add_patch(Polygon(dots, edgecolor='yellow', facecolor='yellow'))
            distance += self.size + self.step

    def tr_rotate(degrees):
        pass


class Polygon_Cust():
    def get_figure(*dots) -> None:
        dots = np.array(list(dots))
        ax.add_patch(Polygon(dots, edgecolor='green', facecolor='green'))


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


# Polygon_Cust.get_figure([0, 0], [15, 10], [20, 20], [20, 15], [10, 0])
# Rectangle_Cust.get_figure(3, 3, 5, 1)
t = Triangle_Cust(5, 2, 1, 'yellow')
t.get_figure()
# Hexagon_Cust.get_figure(3, 3, 1)
