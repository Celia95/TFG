import cmath


class AbstractFunction:
    def __init__(self, f):
        self.f = f


class BoundaryFunction(AbstractFunction):
    def __init__(self, f, steps=300):
        AbstractFunction.__init__(self, f)
        self.__steps = steps

    def eval(self, r, theta):
        if r < 1:
            return self.__integral(-cmath.pi, cmath.pi, self.__steps, r, theta) / (2 * cmath.pi)
        else:
            return self.f(theta)

    def __integral(self, limit_inf, limit_sup, n, r, theta):
        h = (limit_sup - limit_inf) / n
        sum = 0
        for i in range(0, n + 1):
            aux = self.__poisson_integral(r, theta, limit_inf + i * h)
            if (i == 0) or (i == n):
                sum = sum + aux
            else:
                sum = sum + 2 * aux
        return sum * h / 2

    @staticmethod
    def __poisson_kernel(r, theta, t):
        return (1 - r ** 2) / (1 - 2 * r * cmath.cos(theta - t) + r ** 2)

    def __poisson_integral(self, r, theta, t):
        return self.f(t) * self.__poisson_kernel(r, theta, t)


class ComplexFunction(AbstractFunction):
    def __init__(self, f):
        AbstractFunction.__init__(self, f)

    def eval(self, r, theta):
        a = r * cmath.e ** (theta * 1j)
        return self.f(a)


class DifferenceFunction(AbstractFunction):
    def __init__(self, f, g):
        self.__f = f
        self.__g = g

    def eval(self, r, theta):
        return self.__f.eval(r, theta) - self.__g.eval(r, theta)
