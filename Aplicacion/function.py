import cmath


class AbstractFunction:
    def __init__(self, f, label):
        self.f = f
        self.label = label


class BoundaryFunction(AbstractFunction):
    def __init__(self, f, label, steps=300):
        AbstractFunction.__init__(self, f, label)
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
            # aux = f(limit_inf + i * h)
            if (i == 0) or (i == n):
                sum = sum + aux
            else:
                sum = sum + 2 * aux
        return sum * h / 2

    @staticmethod
    def __poisson_kernel(r, theta, t):
        # a = r * cmath.e ** (theta * 1j)
        # return ((cmath.e ** (1j * t) + a) / (cmath.e ** (1j * t) - a)).real
        return (1 - r ** 2) / (1 - 2 * r * cmath.cos(theta - t) + r ** 2)

    def __poisson_integral(self, r, theta, t):
        return self.f(t) * self.__poisson_kernel(r, theta, t)


class ComplexFunction(AbstractFunction):
    def __init__(self, f, label):
        AbstractFunction.__init__(self, f, label)

    def eval(self, r, theta):
        a = r * cmath.e ** (theta * 1j)
        return self.f(a)
