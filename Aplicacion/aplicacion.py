import math
import cmath
import matplotlib.pyplot as plt
import colorsys


def brightness(x):
    if x <= 1:
        return math.sqrt(x) / 2
    else:
        return 1 - 8 / ((x + 3) ** 2)


def complex_color(z):
    if z == 0:
        rgb = colorsys.hsv_to_rgb(0, 1, 0)
    else:
        v = brightness(abs(z))
        h = cmath.phase(z) / (2 * cmath.pi)
        s = (1 - v ** 4) ** 0.25
        rgb = colorsys.hsv_to_rgb(cycle(h), truncate(s), truncate(v))
    return rgb


def truncate(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def cycle(x):
    if x < 0:
        return cycle(x + 1)
    elif x < 1:
        return x
    else:
        return cycle(x - 1)


def f1(t):
    if cmath.pi/2 < t < 3 * cmath.pi/2:
        return 0
    else:
        return 100


def f(t):
    return -20


def integral(f, a, limit):
    return f(limit) * ((cmath.e ** (1j * limit) + a) / (cmath.e ** (1j * limit) - a))


def trapezoidal_rule(f, a, limit_inf, limit_sup):
    return (limit_sup - limit_inf) * (integral(f, a, limit_inf) + integral(f, a, limit_sup)) / 2


def delta(r, step_distance):
    if r == 0:
        return 2 * cmath.pi
    else:
        steps = (2 * cmath.pi * r) / step_distance
        return (2 * cmath.pi) / steps


def poisson(f):
    r = 0
    theta = 0
    step_distance = 0.01
    deltatheta = delta(r, step_distance)
    x = []
    y = []
    rgb = []
    while r <= 1.01:
        while theta < (2 * cmath.pi):
            a = r * cmath.e ** (theta * 1j)
            if r < 1:
                integ = trapezoidal_rule(f, a, -cmath.pi, cmath.pi)
                fa = integ / (2 * cmath.pi)
            else:
                fa = f(theta)
            x.append(a.real)
            y.append(a.imag)
            rgb.append(complex_color(a))
            theta = theta + deltatheta
        r = r + step_distance
        theta = 0
        deltatheta = delta(r, step_distance)
    # plot result
    draw(x, y, rgb)


def draw(x, y, rgb):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    #Move left y-axis and bottim x-axis to centre, passing through (0,0)
    #ax.spines['left'].set_position('center')
    #ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    #ax.grid(True)
    ax.axis('equal')

    # Modify axis
    # plt.xticks([-1, -0.5, 0, +0.5, +1])
    # plt.yticks([-1, -0.5, 0, +0.5, +1])
    #plt.axis([-2, 2, -2, 2])

    plt.title('Prueba')
    plt.scatter(x, y, c=rgb, s=1)
    plt.savefig("disco.png", dpi=700)
    plt.show()


def main():
    poisson(f)


if __name__ == '__main__':
    main()
