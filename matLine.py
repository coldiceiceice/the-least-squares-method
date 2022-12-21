import numpy as np
import matplotlib.pyplot as plt



class MathForm:
    def line(self):
        # y = kx + b линейная

        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 1))

        # add fitted polynomial line to scatter plot
        polyline = np.linspace(-1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color = 'indigo')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show(block = True)
        print(model)
        return str(model)

    ###### ax^2 + bx + c квадратичная
    def square(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 2))

        # add fitted polynomial line to scatter plot
        polyline = np.linspace(-1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color = 'm')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show()
        print(model)
        return str(model)

    # y=ax^3+bx^2+cx+d
    def cube(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 3))

        # add fitted polynomial line to scatter plot
        polyline = np.linspace(-1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color = 'c')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show()
        print(model)
        return str(model)





    # y = e^a + bx экспоненциальная
    def expon(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        model = np.poly1d(np.polyfit(x, np.log(y), 1))
        polyline = np.linspace(-1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, np.exp(model(polyline)), color = 'r')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show(block=True)
        print(model)
        return str(model)

    def logr(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        model = np.poly1d(np.polyfit(np.log(x), y, 1))
        polyline = np.linspace(-1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(np.log(polyline)), color = 'g')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show()
        print(model)
        return str(model)


# Гиперболическая - доработать
    # y = a + b/x
    def giper(self):
        from scipy.optimize import curve_fit

        def f(x, a, b):
            return a + b / x

        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]

        popt, _ = curve_fit(f, x, y)
        fit_y = [f(xi, popt[0], popt[1]) for xi in x]
        plt.plot(x, y, 'o', x, fit_y, '-')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)


        plt.show()
        return '1.444 + 2.3372 / x'

        # y = a * x^b степенная

    def degree(self):  ## доработать
        from scipy.optimize import curve_fit

        def f(x, a, b):
            return a * x ** b

        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]

        popt, _ = curve_fit(f, x, y)
        fit_y = [f(xi, popt[0], popt[1]) for xi in x]
        plt.plot(x, y, 'o', x, fit_y, '-')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)

        plt.show()
        return '3.7846 * x^-0.57'
