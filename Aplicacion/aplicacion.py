import math
import cmath
import time
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
        rgb = colorsys.hsv_to_rgb(decimal_part(h), truncate(s), truncate(v))
    return rgb


def truncate(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def decimal_part(x):
    return x - math.floor(x)


def poisson_kernel(theta, r, t):
    return (1 - r ** 2) / (1 - 2 * r * cmath.cos(theta - t) + r ** 2)


def poisson_integral(f, r, theta, t):
    return f(t) * poisson_kernel(theta, r, t)


def trapezoidal_rule(f, limit_inf, limit_sup, n, r, theta):
    h = (limit_sup - limit_inf) / n
    sum = 0
    for i in range(0, n + 1):
        aux = poisson_integral(f, r, theta, limit_inf + i * h)
        #  aux = f(limit_inf + i * h)
        if (i == 0) or (i == n):
            sum = sum + aux
        else:
            sum = sum + 2 * aux
    return sum * h / 2


def evaluate(f, b, r, theta):
    if b:  # poisson integral
        if r < 1:
            return trapezoidal_rule(f, -cmath.pi, cmath.pi, 300, r, theta) / (2 * math.pi)
        else:
            return f(theta)
    else:  # function
        a = r * cmath.e ** (theta * 1j)
        return f(a)


def delta(r, step_distance):
    if r == 0:
        return 2 * cmath.pi
    else:
        steps = (2 * cmath.pi * r) / step_distance
        return (2 * cmath.pi) / steps


def poisson(f, b): # r=1 - 0.01
    r = 0
    radio=5
    theta = -cmath.pi
    step_distance = 0.01 * radio
    deltatheta = delta(r, step_distance)
    x = []
    y = []
    rgb = []
    while r <= radio + step_distance:
        while theta < (cmath.pi):
            a = r * cmath.e ** (theta * 1j)
            try:
                fa = evaluate(f, b, r, theta)
                rgb.append(complex_color(fa))
                x.append(a.real)
                y.append(a.imag)
            except (ArithmeticError, ValueError):
                pass
            finally:
                theta = theta + deltatheta

        r = r + step_distance
        theta = -cmath.pi
        deltatheta = delta(r, step_distance)
    plot(x, y, rgb)


def plot(x, y, rgb):
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

    plt.title('f(t) = cos^2(t)-sen^2(t)')
    plt.scatter(x, y, c=rgb, s=1)
    plt.savefig("disco.png", dpi=1000)
    #plt.show()


def main():
    start_time = time.time()
    poisson(lambda t: cmath.e ** t, 0)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
