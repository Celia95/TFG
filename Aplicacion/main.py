import cmath
import time

from function import BoundaryFunction
from function import ComplexFunction
from function import DifferenceFunction
from plotter import Plotter


start_time = time.time()

#plotter = Plotter(DifferenceFunction(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2),
#                  ComplexFunction(lambda t: (t ** 2).real)))
#plotter.plot('diff.png', show=False)

#plotter = Plotter(DifferenceFunction(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2),
#                  ComplexFunction(lambda t: t.real ** 2 - t.imag ** 2))) #x^2-y^2
#plotter.plot('diff5.png', show=True)

#plotter = Plotter(DifferenceFunction(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2 + (2 * cmath.cos(t) * cmath.sin(t)) * 1j),
#                  ComplexFunction(lambda t: t ** 2)))
#plotter.plot('diff2.png', show=False)

#plotter = Plotter(DifferenceFunction(BoundaryFunction(lambda t: cmath.cos(t) + 1j * cmath.sin(t)),
#                  ComplexFunction(lambda t: t)))
#plotter.plot('diff4.png', show=False)

#plotter = Plotter(DifferenceFunction(BoundaryFunction(lambda t: cmath.e ** (8 * cmath.cos(t) + 8j * cmath.sin(t))),
#                  ComplexFunction(lambda t: cmath.e ** (8 * t))))
#plotter.plot('diff3.png', show=False)



#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t / 2)))
#plotter.plot('cos(t:2)', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.sin(3 * t)))
#plotter.plot('sen(3t)', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(3 * t) + cmath.sin(3 * t)))
#plotter.plot('cos(3t)+sen(3t).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 3 * cmath.cos(t) + 3j * cmath.sin(t)))
#plotter.plot('3cos(t)+3isen(t).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2))
#plotter.plot('cos^2(t)-sen^2(t).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(t) ** 2 - cmath.sin(t) ** 2 + (2 * cmath.cos(t) * cmath.sin(t)) * 1j))
#plotter.plot('cos^2(t)-sen^2(t)+(2cos(t)sen(t))i.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.e ** (8 * cmath.cos(t) + 8j * cmath.sin(t))))
#plotter.plot('e^(8cos(t)+8isen(t)).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: cmath.cos(3 * t + 1j) + cmath.sin(3 * t + 1j)))
#plotter.plot('cos(3t+i)+sen(3t+i).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 1 / (1 + t ** 2)))
#plotter.plot('1:(1+t^2).png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: t ** 2, 'f(t) = t^2'))
#plotter.plot('t^2.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: t ** 3, 'f(t) = t^3'))
#plotter.plot('t^3.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 0 if -cmath.pi < t < 0 else 100))
#plotter.plot('atrozos.png', show=False)

#plotter = Plotter(BoundaryFunction(lambda t: 20j if -cmath.pi < t < 0 else -20 if 0 <= t < cmath.pi / 2 else 20))
#plotter.plot('atrozos(2).png', show=False)



#plotter = Plotter(ComplexFunction(lambda t: 1/(1-t)))
#plotter.plot('1:(1-z).png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.log(1/(1-t))))
#plotter.plot('log(1:(1-z))(2).png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.cos(t)))
#plotter.plot('cos(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sin(t)))
#plotter.plot('sen(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sin(1/t)))
#plotter.plot('sen(1:z).png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.tan(t)))
#plotter.plot('tan(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.sqrt(t)))
#plotter.plot('sqrt(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.log(t)))
#plotter.plot('log(z).png', show=False, radio=4)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** t))
#plotter.plot('e^z.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** (1 / t)))
#plotter.plot('e^(1:z)2.png', show=False)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** (-t ** 2)))
#plotter.plot('e^(-z^2).png', show=False, radio=5)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** ((t + 1) / (t - 1))))
#plotter.plot('e^((z+1)/(z-1)).png', show=False, radio=2)

#plotter = Plotter(ComplexFunction(lambda t: cmath.e ** cmath.sin(t)))
#plotter.plot('e^(sen(z)).png', show=False, radio=5)

#plotter = Plotter(ComplexFunction(lambda t: 1/(t ** 3 - 1)))
#plotter.plot('1:(z^3 - 1).png', show=False, radio=2)

#plotter = Plotter(ComplexFunction(lambda t: 3*t))
#plotter.plot('3z.png', show=False, radio=1)

#plotter = Plotter(ComplexFunction(lambda t: t ** 2))
#plotter.plot('z^2(2).png', show=False, radio=1)

#plotter = Plotter(ComplexFunction(lambda t: t ** 3))
#plotter.plot('z^3.png', show=False, radio=10)

#plotter = Plotter(ComplexFunction(lambda t: t ** 8 - 2 * t ** 7 + 2 * t ** 6 - 4 * t ** 5 + 2 * t ** 4 - 2 * t ** 3 - 5 * t ** 2 + 4 * t -4))
#plotter.plot('z^8-2z^7+2z^6-4z^5+2z^4-2z^3-5z^2+4z-4.png', show=False, radio=3)

print("--- %s seconds ---" % (time.time() - start_time))

