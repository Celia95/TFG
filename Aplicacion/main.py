import cmath
import time

from function import BoundaryFunction
from function import ComplexFunction
from plotter import Plotter


start_time = time.time()

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t / 2), 'f(t) = cos(t/2)'))
#plotter.plot('cos(t:2)', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.sin(3 * t), 'f(t) = sin(3t)'))
#plotter.plot('sen(3t)', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(3 * t) + cmath.sin(3 * t), 'f(t) = cos(3t) + sen(3t)'))
#plotter.plot('cos(3t) + sen(3t).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2, 'f(t) = cos^2(t)-sen^2(t)'))
#plotter.plot('cos^2(t)-sen^2(t).png', show=False)

plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2 + (2 * cmath.cos(t) * cmath.sin(t)) * 1j, 'f(t) = cos^2(t)-sen^2(t)+[2 cos(t) sen(t)]i'))
plotter.plot('cos^2(t)-sen^2(t)+[2 cos(t) sen(t)]i.png', show=True)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(3 * t + 1j) + cmath.sin(3 * t + 1j), 'f(t) = cos(3t + i) + sen(3t + i)'))
#plotter.plot('cos(3t + i) + sen(3t + i).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 1 / (1 + t ** 2), 'f(t) = 1/(1+t^2)'))
#plotter.plot('1:(1+t^2).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: t ** 2, 'f(t) = t^2'))
#plotter.plot('t^2.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: t ** 3, 'f(t) = t^3'))
#plotter.plot('t^3.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 0 if -cmath.pi < t < 0 else 100, 'Truncada'))
#plotter.plot('truncada.png', show=False)



#plotter = Plotter(ComplexFunction(lambda t: cmath.cos(t), 'f(z) = cos(z)'))
#plotter.plot('cos(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sin(t), 'f(z) = sen(z)'))
#plotter.plot('sen(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sin(1/t), 'f(z) = sen(1/z)'))
#plotter.plot('sen(1:z).png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.tan(t), 'f(z) = tan(z)'))
#plotter.plot('tan(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sqrt(t), 'f(z) = sqrt(z)'))
#plotter.plot('sqrt(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.log(t), 'f(z) = log(z)'))
#plotter.plot('log(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** t, 'f(z) = e^z)'))
#plotter.plot('e^z.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** (1 / t), 'f(z) = e^(1/z)'))
#plotter.plot('e^(1:z)2.png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** (-t ** 2), 'f(z) = e^(-z^2)'))
#plotter.plot('e^(-z^2).png', show=False, radio=5)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** ((t + 1) / (t - 1)), 'f(z) = e^((z+1)/(z-1))'))
#plotter.plot('e^((z+1)/(z-1)).png', show=False, radio=2)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** cmath.sin(t), 'f(z) = e^(sen(z))'))
#plotter.plot('e^(sen(z)).png', show=False, radio=5)

#plotter = Plotter(ComplexFunction(lambda t: 1/(t ** 3 - 1), 'f(z) = 1/(z^3 - 1)'))
#plotter.plot('1:(z^3 - 1).png', show=False, radio=2)

#plotter = Plotter(ComplexFunction(lambda t: t, 'f(z) = z'))
#plotter.plot('z.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: t ** 2, 'f(z) = z^2'))
#plotter.plot('z^2.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: t ** 3, 'f(z) = z^3'))
#plotter.plot('z^3.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: t ** 8 - 2 * t ** 7 + 2 * t ** 6 - 4 * t ** 5 + 2 * t ** 4 - 2 t ** 3 - 5 * t ** 2 + 4 * t -4, 'f(z) = z^8-2z^7+2z^6-4z^5+2z^4-2z^3-5z^2+4z-4'))
#plotter.plot('z^8-2z^7+2z^6-4z^5+2z^4-2z^3-5z^2+4z-4.png', show=False, radio=3)

print("--- %s seconds ---" % (time.time() - start_time))

