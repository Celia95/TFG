import cmath
import math
import matplotlib.pyplot as plt
import colorsys
from misc import frange


class Plotter:
    def __init__(self, abstract_function):
        self.__abstract_function = abstract_function

    def plot(self, file_name="disco.png", show=True, radio=1):
        step_distance = 0.01 * radio
        x = []
        y = []
        rgb = []
        for r in frange(0, radio + step_distance, step_distance):
            delta_theta = self.__delta(r, step_distance)
            for theta in frange(-math.pi, math.pi, delta_theta):
                a = r * cmath.e ** (theta * 1j)
                try:
                    fa = self.__abstract_function.eval(r, theta)
                    rgb.append(self.__complex_color(fa))
                    x.append(a.real)
                    y.append(a.imag)
                except (ArithmeticError, ValueError):
                    pass

        self.__plot(x, y, rgb, self.__abstract_function.label, file_name, show)

    @staticmethod
    def __delta(r, step_distance):
        if r == 0:
            return 2 * cmath.pi
        else:
            steps = (2 * cmath.pi * r) / step_distance
            return (2 * cmath.pi) / steps

    @staticmethod
    def __brightness(x):
        if x <= 1:
            return math.sqrt(x) / 2
        else:
            return 1 - 8 / ((x + 3) ** 2)

    @staticmethod
    def __complex_color(z):
        if z == 0:
            rgb = colorsys.hsv_to_rgb(0, 1, 0)
        else:
            v = Plotter.__brightness(abs(z))
            h = cmath.phase(z) / (2 * cmath.pi)
            s = (1 - v ** 4) ** 0.25
            rgb = colorsys.hsv_to_rgb(Plotter.__decimal_part(h), Plotter.__truncate(s), Plotter.__truncate(v))
        return rgb

    @staticmethod
    def __truncate(x):
        if x < 0:
            return 0
        elif x < 1:
            return x
        else:
            return 1

    @staticmethod
    def __decimal_part(x):
        return x - math.floor(x)

    @staticmethod
    def __plot(x, y, rgb, label, file_name, show):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # Move left y-axis and bottim x-axis to centre, passing through (0,0)
        # ax.spines['left'].set_position('center')
        # ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # ax.grid(True)
        ax.axis('equal')

        # Modify axis
        # plt.xticks([-1, -0.5, 0, +0.5, +1])
        # plt.yticks([-1, -0.5, 0, +0.5, +1])
        # plt.axis([-2, 2, -2, 2])

        plt.title(label)
        plt.scatter(x, y, c=rgb, s=1)
        plt.savefig(file_name, dpi=1000)
        if show:
            plt.show()
