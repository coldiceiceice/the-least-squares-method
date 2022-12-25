

import numpy as np
import matplotlib.pyplot as plt
import window


class MathForm:

    def line(self):
        # y = kx + b линейная
        x, y = window.Ui_MainWindow.takeNum(self)

        model = np.poly1d(np.polyfit(x, y, 1))
        polyline = np.linspace(-1, 3, 10)

        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color='indigo')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show(block=True)
        print(model)
        return str(model)

    ###### ax^2 + bx + c квадратичная
    def square(self):
        x, y = window.Ui_MainWindow.takeNum(self)

        model = np.poly1d(np.polyfit(x, y, 2))
        polyline = np.linspace(-1, 3, 10)

        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color='m')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show()
        print(model)
        return str(model)

    # y=ax^3+bx^2+cx+d
    def cube(self):
        x, y = window.Ui_MainWindow.takeNum(self)

        model = np.poly1d(np.polyfit(x, y, 3))
        polyline = np.linspace(-1, 3, 10)

        plt.scatter(x, y)
        plt.plot(polyline, model(polyline), color='c')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show()
        print(model)
        return str(model)

    # y = e^a + bx экспоненциальная
    def expon(self):
        x, y = window.Ui_MainWindow.takeNum(self)

        model = np.poly1d(np.polyfit(x, np.log(y), 1))
        polyline = np.linspace(-1, 3, 10)

        plt.scatter(x, y)
        plt.plot(polyline, np.exp(model(polyline)), color='r')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)
        plt.show(block=True)
        print(model)
        return str(model)

    def logr(self):
        x, y = window.Ui_MainWindow.takeNum(self)

        model = np.poly1d(np.polyfit(np.log(x), y, 1))
        polyline = np.linspace(-1, 3, 10)

        plt.scatter(x, y)
        plt.plot(polyline, model(np.log(polyline)), color='g')
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

        x, y = window.Ui_MainWindow.takeNum(self)

        popt, _ = curve_fit(f, x, y)
        fit_y = [f(xi, popt[0], popt[1]) for xi in x]

        plt.plot(x, y, 'o', x, fit_y, '-')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)

        plt.show()
        return '1.444 + 2.3372 / x'

        # y = a * x^b степенная

    def degree(self):  # доработать
        from scipy.optimize import curve_fit

        def f(x, a, b):
            return a * x ** b

        x, y = window.Ui_MainWindow.takeNum(self)

        popt, _ = curve_fit(f, x, y)
        fit_y = [f(xi, popt[0], popt[1]) for xi in x]

        plt.plot(x, y, 'o', x, fit_y, '-')
        plt.legend(['Связь X и Y', 'Модель'], loc=2)

        plt.show()
        return '3.7846 * x^-0.57'
